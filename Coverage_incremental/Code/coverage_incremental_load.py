import csv
import sys
import math
import numpy
import random
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, text, func

#Import file truncate
import truncate_table as tt

#Importing configuration file
sys.path.insert(0, "../Config")
import Config_coverage_il as Cconf


#connect to postgres
engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')
db_connection = engine.connect()
	
#read coverage table from database
select = text("SELECT * FROM coverage")
result = db_connection.execute(select)
reader_coverage_data = pd.DataFrame(list(result), columns = result.keys())

coverage_list = []


#updates coverage table with regard to updated policy table
def append_new_policy():
	global coverage_list

	#read policy incremental table from database
	select = text("SELECT * FROM policy_il")
	result = db_connection.execute(select)
	reader_policy_inc = pd.DataFrame(list(result), columns = result.keys())
	unique_policies = reader_policy_inc['policynumber'].unique().tolist()
	reader_policy_inc = reader_policy_inc[['policynumber', 'termeffectivedate', 'termexpirationdate','policyaddressid', 'policystatus', 'recordstartdate']]

	#read policy table from database
	select = text("SELECT * FROM policy")
	result = db_connection.execute(select)
	policy_numbers = pd.DataFrame(list(result), columns = result.keys())['policynumber'].unique().tolist()
	
	#read coverage table from database
	select = text("SELECT * FROM coverage")
	result = db_connection.execute(select)
	reader_coverage = pd.DataFrame(list(result), columns = result.keys())
	reader_coverage = reader_coverage[['coverage_id', 'coverage_name', 'vin', 'policy_number']]
	
	#read coverage limit table from database
	select = text("SELECT * FROM coverage_limit")
	result = db_connection.execute(select)
	reader_coverage_data = pd.DataFrame(list(result), columns = result.keys())
	BI = reader_coverage_data[reader_coverage_data['coverage'] == 'BI'].values.tolist()
	PD = reader_coverage_data[reader_coverage_data['coverage'] == 'PD'].values.tolist()

	#read customer table from database
	select = text("SELECT * FROM customer")
	result = db_connection.execute(select)
	reader_customer_data = pd.DataFrame(list(result), columns = result.keys())[['address_id', 'license']]

	#read vehicle table from database
	select = text("SELECT * FROM vehicle")
	result = db_connection.execute(select)
	reader_vin_data = pd.DataFrame(list(result), columns = result.keys())[['vin', 'license_plate_no']]

	new_policy_numbers = reader_policy_inc[reader_policy_inc['policynumber'] > policy_numbers[len(policy_numbers)-1]]['policynumber'].values.tolist()
	cancelled_policies = reader_policy_inc[reader_policy_inc['policystatus'] == "Cancelled"]['policynumber'].values.tolist()
	
	end_date = ""
	update_date = ""
	i=0

	#For new policies add coverages
	while(i < len(new_policy_numbers)):
		#Randomly decide if a policy should have 2 or 3 coverages
	    	total_coverages = numpy.random.choice([2,3],p=[0.5,0.5])
	    	current_policy = reader_policy_inc[reader_policy_inc['policynumber'] == new_policy_numbers[i]].values.tolist()
	    	policy_no = current_policy[0][0]
	    	family_id = current_policy[0][3]
		status = current_policy[len(current_policy)-1][4]
	    	license_plates = reader_customer_data.loc[reader_customer_data['address_id'] == family_id]['license'].values.tolist()
		start_date = datetime.now()

    	    	k = 0
	
	    	while(k < len(license_plates)):
	       		VIN = reader_vin_data.loc[reader_vin_data['license_plate_no'] == license_plates[k]]['vin'].values.tolist()[0]
	
	       		if VIN != []:
				j = 0
	
	        		while(j < total_coverages):
					# select coverage limit compulsory BI coverage
	       				if j == 0:
				            	cov_BI = random.choice(BI)
						cov_name = "BI"
	       					coverage_list.append([cov_BI[0],cov_name,VIN,policy_no, start_date,end_date,update_date])

					#select coverage limit Compulsory PD coverage
				        elif j == 1:
	            				cov_PD = random.choice(PD)
						cov_name = "PD"
				                coverage_list.append([cov_PD[0],cov_name,VIN,policy_no, start_date,end_date,update_date])

					#select coverage limit Optional random coverage
			        	else:
						cov_name = random.choice(["Uninsured", "Underinsured", "Medical Payments"])
	            				cov_other = random.choice(reader_coverage_data[reader_coverage_data['coverage'] == cov_name].values.tolist())
						coverage_list.append([cov_other[0],cov_name,VIN,policy_no, start_date,end_date,update_date])
	
	        			j = j + 1
			k = k + 1
	
	    	i = i + 1
		
	i = 0

	#For existing policies add end date to existing policies
	while(i < len(cancelled_policies)):
		current_policy = reader_policy_inc[reader_policy_inc['policynumber'] == cancelled_policies[i]].values.tolist()
		start_date = current_policy[0][5]
		coverage_row = reader_coverage[reader_coverage['policy_number'] == cancelled_policies[i]].values.tolist()
		j = 0

		while(j < len(coverage_row)):
			coverage_id = coverage_row[j][0]
			coverage_name = coverage_row[j][1]
			VIN = coverage_row[j][2]
			policy_no = coverage_row[j][3]
			coverage_list.append([coverage_id,coverage_name,VIN,policy_no, start_date,end_date,update_date])
			j = j + 1

		i = i + 1
				

def change_coverage_limit():
   	global coverage_list
	VIN = reader_coverage_data['vin'].unique().tolist()
    	coverage_id = reader_coverage_data['coverage_id'].unique().tolist()
    	num_records = random.randint(Cconf.min_records_for_limits,Cconf.max_records_for_limits)
    	end_date = ""
    	update_date = ""
    	i = 0

	#Find existing limit and choose different limit for existing coverage
    	def get_coverage_limit(coverage_id,temp_list):
        	limit_id = random.choice([x for x in coverage_id if x not in temp_list])
	
	        if int(limit_id.split('COV01-10000')[1]) <= 7:
	            	return 0,limit_id

       		elif int(limit_id.split('COV01-10000')[1]) > 7 and int(limit_id.split('COV01-10000')[1]) <= 14:
            		return 1,limit_id

       		elif len(temp_list) == 2 and int(limit_id.split('COV01-10000')[1]) > 14:
            		flag, new_limit_id = get_coverage_limit(coverage_id,temp_list)
       	    		return flag,new_limit_id

       		else:
            		return 2,limit_id
       
    	while(i < num_records):
       		current_VIN = random.choice(VIN)
        	temp_list = reader_coverage_data.loc[reader_coverage_data['vin'] == current_VIN]['coverage_id'].values.tolist()
	        flag, new_limit_id = get_coverage_limit(coverage_id,temp_list)
		
		if flag == 0:
			cov_name = "BI"

		elif flag == 1:
			cov_name = "PD"

		else:
			if int(new_limit_id.split('COV01-10000')[1]) >= 15 and int(new_limit_id.split('COV01-10000')[1]) <= 21:
				cov_name = "Uninsured"

			elif int(new_limit_id.split('COV01-10000')[1]) >= 22 and int(new_limit_id.split('COV01-10000')[1]) <= 28:
				cov_name = "Underinsured"

			else:
				cov_name = "Medical Payments"

	        policy_no = reader_coverage_data.loc[(reader_coverage_data['vin'] == current_VIN) & (reader_coverage_data['coverage_id'] == temp_list[flag])]['policy_number'].values.tolist()[0]
	        temp_list[flag] = new_limit_id
        	coverage_list.append([temp_list[flag],cov_name,current_VIN, policy_no, datetime.now(), end_date, update_date])
	        i = i + 1



#Add or remove coverage limits
def modify_existing_policy():
	global coverage_list
    	policies = reader_coverage_data['policy_number'].unique().tolist()
    	num_records = random.randint(Cconf.min_records_for_modify,Cconf.max_records_for_modify)
    	end_date = ""
    	update_date = ""
    	i = 0
    	prefix = '0'
    
    	def add_new_coverage():
		#add random coverage with random limit
		random_number =	random.randint(15,32)

		if random_number > 14 and random_number < 22:
			cov_name = "Uninsured"

		elif random_number >= 22 and random_number < 29:
			cov_name = "Underinsured"

		else:
			cov_name = "Medical Payments"

	        coverage_id = "COV01-10000"+str(random_number)
	        coverage_list.append([coverage_id,cov_name,current_VIN,current_policy,datetime.now(),end_date,update_date])

       
    	def remove_existing_coverage(i):
		end_date = reader_coverage_data.loc[(reader_coverage_data['vin'] == current_VIN) & (reader_coverage_data['coverage_id'] == temp_cov_list[2])]['record_end_date'].values.tolist()[0]
		
		#Checks if end_date is null
		if end_date != end_date:
	        	coverage_id = temp_cov_list[2]

			if int(coverage_id.split('COV01-10000')[1]) >= 15 and int(coverage_id.split('COV01-10000')[1]) <= 21:
				cov_name = "Uninsured"

			elif int(coverage_id.split('COV01-10000')[1]) >= 22 and int(coverage_id.split('COV01-10000')[1]) <= 28:
				cov_name = "Underinsured"

			else:
				cov_name = "Medical Payments"

		        coverage_list.append([coverage_id,cov_name,current_VIN,current_policy,datetime.now(),end_date,update_date])
		else:
			i = i - 1
    
    	while(i < num_records):
        	current_policy = random.choice(policies)
	        temp_vin_list = reader_coverage_data.loc[reader_coverage_data['policy_number'] == current_policy]['vin'].values.tolist()
	        current_VIN = random.choice(temp_vin_list)
		end_date = reader_coverage_data.loc[(reader_coverage_data['policy_number'] == current_policy) & (reader_coverage_data['vin'] == current_VIN)]['record_end_date'].values.tolist()[0]
		
		#Checks if end_date is null
		if end_date == None:
			temp_cov_list = reader_coverage_data.loc[(reader_coverage_data['vin'] == current_VIN)]['coverage_id'].values.tolist()

			#if there are 2 coverages for selected policy then add a coverage else remove one coverage
	        	if len(temp_cov_list) == 2:
		      		add_new_coverage()

			elif len(temp_cov_list) == 3:
			       	remove_existing_coverage(i)

			i = i + 1
		else:
			i = i - 1
			continue
def main():
	append_new_policy()
	change_coverage_limit()
	modify_existing_policy()

	#truncate table if already exists
	if engine.dialect.has_table(engine, Cconf.table_name):
		tt.truncate(Cconf.table_name)

	#Create table with specified columns
	df = pd.DataFrame.from_records(coverage_list, columns=Cconf.headers)

	#Convert date to datetime
	df["record_start_date"] =  pd.to_datetime(df["record_start_date"])
	df["record_end_date"] =  pd.to_datetime(df["record_end_date"])
	df["record_update_date"] =  pd.to_datetime(df["record_update_date"])

	#Load the table to database
	df.to_sql(Cconf.table_name, engine, index=False)

	if engine.dialect.has_table(engine, 'coverage_bkp'):
		tt.truncate('coverage_bkp')
	
	select = text("CREATE TABLE coverage_bkp AS SELECT * FROM coverage")
	db_connection.execution_options(autocommit=True).execute(select)

	select = text("SELECT * FROM coverage_il")
	result = db_connection.execute(select)
	test = pd.DataFrame(list(result), columns = result.keys())
	print(test.head(40))

	select = text("SELECT scd2_coverage_2()")
	db_connection.execution_options(autocommit=True).execute(select)

	select = text("SELECT * FROM coverage_bkp")
	result = db_connection.execute(select)
	test = pd.DataFrame(list(result), columns = result.keys())
	print(test.tail(50))

	print(str(len(coverage_list))+" Records generated and written to the db.")

if __name__ == "__main__":
	main()