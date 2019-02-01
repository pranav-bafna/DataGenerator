# Import all required modules
import csv
import random
import sys
sys.path.insert(0, '../configuration')

import policy_config as pc
import output_file_paths as ofp

from random import randint
import numpy
import datetime
import time
from dateutil.relativedelta import relativedelta

from faker import Faker
fake = Faker()

import pandas as pd
from sqlalchemy import create_engine, select, MetaData, Table, text
import psycopg2

import coverage_generator
engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')

metadata = MetaData(bind=None)
table = Table(ofp.table_name, metadata, autoload = True, autoload_with = engine)
stmt = select([table])
headers = metadata.tables[ofp.table_name].columns.keys()
connection = engine.connect()

# read customers data
customer_data = connection.execute(stmt).fetchall()
customer_data = pd.DataFrame(customer_data,columns = headers)

def main():
	final_data = []

	contactid_data = csv.reader(open(pc.contact_id_file))
	contactid_data.next()
	id_data = list(contactid_data)

	status_lst = ["Active","Lapsed","Inactive","Cancelled"]

	# For no of policies mentioned in the config file
	for i in range(0,pc.total_records):
		source = numpy.random.choice(pc.source)

		policy = id_data[i][5]

		LOB = "Auto"
		type = "Auto Insurance"
		address_id = id_data[i][4]

		# get state from customers data
		state = customer_data[customer_data['address_id'] == address_id]["residential_state"].values[0]	

		renewal_terms_tot = random.choice([1,2,3])
		renewal_cycle = random.choice([6,12])

		# Generate random inception date based on probabilties

		p=[]
		year_lst = []
		for k, v in pc.inception_year_probabilty.iteritems():
			year = k.split("-")
			p.append(v)

			if year[0] == "current_year":
				year_lst.append(int(time.strftime("%Y")))
			else:
				year_lst.append(randint(int(year[0]),int(year[1])))
				
		inception_year = numpy.random.choice(year_lst, p=p)

		if inception_year==int(time.strftime("%Y")):
			month = int(time.strftime("%m"))
			day = int(time.strftime("%d"))
		else:
			month = random.choice(range(1,13))
    			if month == 2:
        			day = random.choice(range(1, 29))
    			else:
        			day = random.choice(range(1, 31))

    		inception_date = datetime.date(inception_year, month, day)

		reason = ""
		status = ""
		term = 1
		status_hist = []

		while(True):
			if term == 1:
				status = "Active"
			else:
				status = numpy.random.choice(status_lst, p=[0.9, 0.03, 0.03, 0.04])
		
			random_choice = random.choice(["prev","curr"])
			if term == 1 or random_choice == "prev" or status == "Active":
				if term==1:
					eff_date = inception_date

				else:
					eff_date = last_eff_date + relativedelta(months=renewal_cycle)
				exp_date = eff_date + relativedelta(months=renewal_cycle)
				start_date = eff_date
			else:
				eff_date = last_eff_date
				exp_date = last_exp_date
				start_date = last_end_date
				term = term - 1
			
			last_eff_date = eff_date
			last_exp_date = exp_date

			pre_amount = "$" + str(random.randint(500,2000))

			if exp_date > datetime.date.today() or status in ["Inactive","Lapsed","Cancelled"]:
				end_date = ""
			else:
				end_date = exp_date

			
			last_end_date = end_date

			final_data.append([source,policy,LOB,type,state,address_id,eff_date,exp_date,inception_date,renewal_cycle,term,status,reason,pre_amount,start_date,end_date])

			term = term + 1
			status_hist.append(status)
			if exp_date > datetime.date.today() or status in ["Inactive","Lapsed","Cancelled"]:
				break
		

	df = pd.DataFrame.from_records(final_data, columns=pc.headers)
	
	df["termeffectivedate"] =  pd.to_datetime(df["termeffectivedate"])
	df["termeffectivedate"] = df["termeffectivedate"].dt.date

	df["termexpirationdate"] =  pd.to_datetime(df["termexpirationdate"])
	df["termexpirationdate"] = df["termexpirationdate"].dt.date

	df["policyinceptiondate"] =  pd.to_datetime(df["policyinceptiondate"])
	df["policyinceptiondate"] = df["policyinceptiondate"].dt.date

	df["recordstartdate"] =  pd.to_datetime(df["recordstartdate"])
	df["recordstartdate"] = df["recordstartdate"].dt.date

	df["recordenddate"] =  pd.to_datetime(df["recordenddate"])
	df["recordenddate"] = df["recordenddate"].dt.date

	engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')
	# write data to postgres
	df.to_sql(pc.table_name, engine, index=False, if_exists='replace')


if __name__=="__main__":
	main()


