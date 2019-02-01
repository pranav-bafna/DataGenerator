import csv
import sys
import time
import numpy
import random
import psycopg2
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, text


#Import file coverage limit generator
import coverage_limit_generator as cl

#Import file truncate
import truncate_table as tt

#Import configuration file
sys.path.insert(0, "../Config")
import Config_CovGen as CConf

def generate_coverage():
	cov_limits = []
	VIN_list = []
	policy_list = []
	coverage_list = []

	#connect to postgres
	engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')
	db_connection = engine.connect()

	#load data from policy table
	select = text("SELECT * FROM policy")
	result = db_connection.execute(select)
	reader_policy_data = pd.DataFrame(list(result), columns = result.keys())
	unique_policies = reader_policy_data['policynumber'].unique().tolist()
	reader_policy_data = reader_policy_data[['policynumber', 'termeffectivedate', 'recordstartdate','policyaddressid', 'policystatus']]

	#load data from coverage limits table	
	select = text("SELECT * FROM coverage_limit")
	result = db_connection.execute(select)
	reader_coverage_data = pd.DataFrame(list(result), columns = result.keys())
	BI = reader_coverage_data[reader_coverage_data['coverage'] == 'BI'].values.tolist()
	PD = reader_coverage_data[reader_coverage_data['coverage'] == 'PD'].values.tolist()

	#load data from customer table
	select = text("SELECT * FROM customer")
	result = db_connection.execute(select)
	reader_customer_data = pd.DataFrame(list(result), columns = result.keys())[['address_id', 'license']]

	#load data from vehicle table
	select = text("SELECT * FROM vehicle")
	result = db_connection.execute(select)
	reader_vin_data = pd.DataFrame(list(result), columns = result.keys())[['vin', 'license_plate_no']]
	#reader_vin_data = pd.read_csv('/elastic_search_test/vehicle_data_1L.csv')[['VIN', 'License Plate No']]
	
	i = 0
	start = time.time()
	while(i < len(unique_policies)):
		#Randomly choose whether to have 2 or 3 coverages
	    	total_coverages = numpy.random.choice([2,3],p=[0.5,0.5])
	    	current_policy = reader_policy_data[reader_policy_data['policynumber'] == unique_policies[i]].values.tolist()
	    	policy_no = current_policy[0][0]
	    	start_date = current_policy[0][1]
	    	family_id = current_policy[0][3]
		status = current_policy[len(current_policy)-1][4]
    	    	license_plates = reader_customer_data.loc[reader_customer_data['address_id'] == family_id]['license'].values.tolist()

    	    	k = 0

	    	while(k < len(license_plates)):
            		VIN = reader_vin_data.loc[reader_vin_data['license_plate_no'] == license_plates[k]]['vin'].values.tolist()[0]

            		if VIN != []:
				j = 0

	        		while(j < total_coverages):

					if status == "Cancelled":
						end_date = str(current_policy[len(current_policy)-1][2])

					else:
						end_date = ""

					#select compulsory BI coverage and random limit
	        			if j == 0:
				            	cov_BI = random.choice(BI)
						cov_name = "BI"
						upadate_date = end_date
	            				coverage_list.append([cov_BI[0],cov_name,VIN,policy_no, start_date, end_date, upadate_date])

					#select compulsory PD coverage and random limit
				        elif j == 1:
	            				cov_PD = random.choice(PD)
						cov_name = "PD"
						upadate_date = end_date
				                coverage_list.append([cov_PD[0],cov_name,VIN,policy_no, start_date, end_date, upadate_date])

					#select optional random coverage and random limit
				        else:
						cov_name = random.choice(["Uninsured", "Underinsured", "Medical Payments"])
	            				cov_other = random.choice(reader_coverage_data[reader_coverage_data['coverage'] == cov_name].values.tolist())
						if status == "Cancelled":
							coverage_list.append([cov_other[0],cov_name,VIN,policy_no, start_date, end_date, upadate_date])
						else:
		            				end_date = str(numpy.random.choice([current_policy[random.randint(0,len(current_policy)-1)][2],""],p=[0.4,0.6]))	    				
							coverage_list.append([cov_other[0],cov_name,VIN,policy_no, start_date, end_date, upadate_date])

	        			j = j + 1
			k = k + 1

	    	i = i + 1

	gen = time.time()
	print("Generate: "+str(gen-start))
	
	#Truncate table if already exists
	if engine.dialect.has_table(engine, CConf.c_table_name):
		tt.truncate(CConf.c_table_name)
	
	#Create table with the specified columns
	df = pd.DataFrame.from_records(coverage_list, columns=CConf.c_headers)

	#Convert to datetime
	df["record_start_date"] =  pd.to_datetime(df["record_start_date"])
	df["record_end_date"] =  pd.to_datetime(df["record_end_date"])
	df["record_update_date"] =  pd.to_datetime(df["record_update_date"])

	#load to database
	df.to_sql(CConf.c_table_name, engine, index=False)

	print(str(len(coverage_list))+" records written to DB in "+str(time.time()-gen))
	
def main():
	cl.generate_coverage_list()
	generate_coverage()

if __name__ == "__main__":
	main()
