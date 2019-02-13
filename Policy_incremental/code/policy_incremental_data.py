####################################################################
try:
	import os
	import logging
	import time
	import traceback
	if not os.path.exists(r'../logs'):
		os.makedirs(r'../logs')

	timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
	log_file = "../logs/policy_incremental_log_" + timestamp + ".log"
	logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
	logging.debug("generation of policy incremental script started executing...")
except Exception,e:
	print str(e)

####################################################################

# Import all required modules

try:

	from random import randint
	from datetime import datetime,date
	import pandas as pd
	from sqlalchemy import create_engine, select, MetaData, Table, text
	import datetime as dt
	import sys
	sys.path.insert(0, '../configuration')

	import psycopg2
	import numpy
	import csv
	import random
	from dateutil.relativedelta import relativedelta
	import policy_config as pc
	import output_file_paths as ofp
	import database_credentials as dc

	import json
except Exception,e:
	print str(e)
	logging.debug(traceback.format_exc())
	exit()

logging.debug("Successfully imported all the required modules")

try:
	engine = create_engine(dc.connection_string)
	connection = engine.connect()
	logging.debug("Connection to postgres database is successful")
except Exception,e:
	print "Error Connection issue..."
	logging.debug(traceback.format_exc())
	exit()


ts = time.time()

try:
	logging.debug("Reading policy table data")
	metadata = MetaData(bind=None)
	table = Table(pc.table_name, metadata, autoload = True, autoload_with = engine)
	stmt = select([table])
	policy_headers = metadata.tables[pc.table_name].columns.keys()
	connection = engine.connect()

	global policy_data
	policy_data = connection.execute(stmt).fetchall()
	policy_data = pd.DataFrame(policy_data,columns = policy_headers)

	logging.debug("Reading customers table data")
	metadata = MetaData(bind=None)
	table = Table(ofp.table_name, metadata, autoload = True, autoload_with = engine)
	stmt = select([table])
	customer_headers = metadata.tables[ofp.table_name].columns.keys()

	customer_data = connection.execute(stmt).fetchall()
	customer_data = pd.DataFrame(customer_data,columns = customer_headers)
	global final_df
	final_df = pd.DataFrame(columns = policy_headers)
except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

####################################################################
def create_new_data():
	logging.debug("Creating policy incremental data for new policies")
	global policy_data
	global final_df
	final_data = []

	data = policy_data["policynumber"].str.split("-", n = 1, expand = True)	
	curr_count = int(data[data[1]==data[1].max()][1].values.tolist()[0])

	last_pol = "POL01-"
	last_con = "CNT01-"
	#curr_count = 1025000
	try:
		for i in range(0,15):
			source = numpy.random.choice(["System1","System2","System3"])
			policy = last_pol + str(curr_count + 1)
			address_id = last_con + str(curr_count + 1)
			LOB = "Auto"
			type = "Auto Insurance"

			renewal_cycle = random.choice([6,12])
			inception_date = date.today()

			eff_date = date.today()#datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
			reason = ""
			status = "Active"
			term = 1
			exp_date = eff_date + relativedelta(months=renewal_cycle)

			end_date = ""
			pre_amount = "$" + str(random.randint(500,2000))

			state = customer_data[customer_data['address_id'] == address_id]["residential_state"].values[0]

			curr_count = curr_count + 1

			final_data.append([source,policy,LOB,type,state,address_id,eff_date,exp_date,inception_date,renewal_cycle,term,status,reason,pre_amount,datetime.now(),end_date])
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	try:
		df = pd.DataFrame.from_records(final_data, columns=policy_headers)
	
		df["termeffectivedate"] =  pd.to_datetime(df["termeffectivedate"])
		#df["termeffectivedate"] = df["termeffectivedate"].dt.date

		df["termexpirationdate"] =  pd.to_datetime(df["termexpirationdate"])
		#df["termexpirationdate"] = df["termexpirationdate"].dt.date

		df["policyinceptiondate"] =  pd.to_datetime(df["policyinceptiondate"])
		#df["policyinceptiondate"] = df["policyinceptiondate"].dt.date

		df["recordstartdate"] =  pd.to_datetime(df["recordstartdate"])
		#df["recordstartdate"] = df["recordstartdate"].dt.date

		df["recordenddate"] =  pd.to_datetime(df["recordenddate"])
		#df["recordenddate"] = df["recordenddate"].dt.date

		final_df = final_df.append(df)
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	logging.debug("Successfully created policy incremental data for new policies")


####################################################################
def change_policy_status():
	logging.debug("Creating policy incremental data for change in policy status cases")
	global policy_data
	global final_df

	policy_data = policy_data[policy_data["recordenddate"].isnull()]
	sample_policy = policy_data.sample(n=10)

	try:
		for index,row in sample_policy.iterrows():
			if row["policystatus"]=="Active":
				status = random.choice(["Inactive","Lapsed","Cancelled"])
				sample_policy.ix[index,"policystatus"]=status 
			elif row["policystatus"]=="Inactive":
				status = random.choice(["Active","Cancelled"])
				sample_policy.ix[index,"policystatus"]=status
			elif row["policystatus"]=="Lapsed":
				status = random.choice(["Active","Cancelled","Inactive"])
				sample_policy.ix[index,"policystatus"]=status
			elif row["policystatus"]=="Cancelled":
				sample_policy.ix[index,"policystatus"]="Active"

			sample_policy["recordstartdate"] = datetime.now()
			sample_policy["recordenddate"] = None
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()
	

	try:	
		sample_policy["termeffectivedate"] =  pd.to_datetime(sample_policy["termeffectivedate"])
		#sample_policy["termeffectivedate"] = sample_policy["termeffectivedate"].dt.date

		sample_policy["termexpirationdate"] =  pd.to_datetime(sample_policy["termexpirationdate"])
		#sample_policy["termexpirationdate"] = sample_policy["termexpirationdate"].dt.date

		sample_policy["policyinceptiondate"] =  pd.to_datetime(sample_policy["policyinceptiondate"])
		#sample_policy["policyinceptiondate"] = sample_policy["policyinceptiondate"].dt.date

		sample_policy["recordstartdate"] =  pd.to_datetime(sample_policy["recordstartdate"])
		#sample_policy["recordstartdate"] = sample_policy["recordstartdate"].dt.date

		sample_policy["recordenddate"] =  pd.to_datetime(sample_policy["recordenddate"])
		#sample_policy["recordenddate"] = sample_policy["recordenddate"].dt.date

		#sample_policy.to_sql(pc.table_il, engine, index=False, if_exists='append')
		final_df = final_df.append(sample_policy)
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	logging.debug("Successfully created policy incremental data for change in policy status case")


####################################################################	
def renew_policy():
	logging.debug("Creating policy incremental data for policy renewals")
	global policy_data
	global final_df

	policy_data = policy_data[policy_data["recordenddate"].isnull()]

	#sample_policy= policy_data[policy_data["termexpirationdate"] == str(datetime.today()).split()[0]]
	sample_policy= policy_data[policy_data["termexpirationdate"] == datetime.today().date()]


	sample_policy["recordstartdate"] = datetime.now()
	sample_policy["recordenddate"] = None

	try:
		for index,row in sample_policy.iterrows():
			sample_policy.ix[index,"policystatus"]="Active"
			sample_policy.ix[index,"termexpirationdate"]= sample_policy.ix[index,"termexpirationdate"] + relativedelta(months=sample_policy.ix[index,"renewal_cycle"])
			sample_policy.ix[index,"termeffectivedate"]=sample_policy.ix[index,"termeffectivedate"] + relativedelta(months=sample_policy.ix[index,"renewal_cycle"])
			sample_policy.ix[index,"renewalterm"]=sample_policy.ix[index,"renewalterm"]+ 1

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()


	try:
		sample_policy["termeffectivedate"] =  pd.to_datetime(sample_policy["termeffectivedate"])
		#sample_policy["termeffectivedate"] = sample_policy["termeffectivedate"].dt.date

		sample_policy["termexpirationdate"] =  pd.to_datetime(sample_policy["termexpirationdate"])
		#sample_policy["termexpirationdate"] = sample_policy["termexpirationdate"].dt.date

		sample_policy["policyinceptiondate"] =  pd.to_datetime(sample_policy["policyinceptiondate"])
		#sample_policy["policyinceptiondate"] = sample_policy["policyinceptiondate"].dt.date

		sample_policy["recordstartdate"] =  pd.to_datetime(sample_policy["recordstartdate"])
		#sample_policy["recordstartdate"] = sample_policy["recordstartdate"].dt.date

		sample_policy["recordenddate"] =  pd.to_datetime(sample_policy["recordenddate"])
		#sample_policy["recordenddate"] = sample_policy["recordenddate"].dt.date

		#sample_policy.to_sql(pc.table_il, engine, index=False, if_exists='append')
		final_df = final_df.append(sample_policy)
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	logging.debug("Successfully created policy incremental data for policy renewals")



####################################################################
def main():
	try:

		logging.debug("Generating policy incremental data")
		create_new_data()
		change_policy_status()
		renew_policy()

		final_df["recordstartdate"] =  pd.to_datetime(final_df["recordstartdate"], unit = "s")
		final_df["recordenddate"] =  pd.to_datetime(final_df["recordenddate"], unit = "s")

		engine = create_engine(dc.connection_string)

		final_df.to_sql(pc.table_il, engine, index=False, if_exists='replace')
		logging.debug("Successfully loaded policy incremental data to database")
		final_df['recordstartdate'] = final_df['recordstartdate'].dt.round('1s')
		#final_df.astype(str).to_json('data.json', orient='records', lines=True, date_format='iso')

		#time.sleep(10)
		#query = text("SELECT scd2_policy()")
		#connection.execution_options(autocommit=True).execute(query)
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()


if __name__=="__main__":
	main()