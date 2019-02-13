import os
import time
import logging
import traceback

if not os.path.exists(r'../logs'):
	os.makedirs(r'../logs')

timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
log_file = "../logs/coverage_generator_" + timestamp + ".log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.debug("Coverage data generation is started.")

try:
	import csv
	import sys
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

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

def generate_coverage():
	cov_limits = []
	VIN_list = []
	policy_list = []
	coverage_list = []

	try:
		#connect to postgres
		engine = create_engine(CConf.connection_string)
		db_connection = engine.connect()
		logging.debug("Connected to: "+CConf.connection_string)

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	try:
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
		
		logging.debug("Data loaded.")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	i = 0
	start = time.time()

	try:
		while(i < len(unique_policies)):
			#Randomly choose whether to have 2 or 3 coverages
		    	total_coverages = numpy.random.choice([2,3],p=CConf.cov_probability)
	
			#Select one policy incrementally and make it current policy
		    	current_policy = reader_policy_data[reader_policy_data['policynumber'] == unique_policies[i]].values.tolist()

			#Extract data from the current policy
		    	policy_no = current_policy[0][0]
		    	start_date = current_policy[0][1]
		    	family_id = current_policy[0][3]
			status = current_policy[len(current_policy)-1][4]
	    	    	license_plates = reader_customer_data.loc[reader_customer_data['address_id'] == family_id]['license'].values.tolist()

    		    	k = 0

	    		while(k < len(license_plates)):
				#For all vehicles in the same policy
	            		VIN = reader_vin_data.loc[reader_vin_data['license_plate_no'] == license_plates[k]]['vin'].values.tolist()[0]

	            		if VIN != []:
					j = 0

		        		while(j < total_coverages):
						if status == "Cancelled":
							end_date = str(current_policy[len(current_policy)-1][2])
							coverage_status = "Inactive"

						else:
							coverage_status = "Active"
							end_date = ""

						#select compulsory BI coverage and random limit
		        			if j == 0:
					            	cov_BI = random.choice(BI)
							cov_name = "BI"
							upadate_date = end_date
	            					coverage_list.append([cov_BI[0],cov_name,VIN,policy_no, coverage_status, start_date, end_date, upadate_date])

						#select compulsory PD coverage and random limit
					        elif j == 1:
	        	    				cov_PD = random.choice(PD)
							cov_name = "PD"
							upadate_date = end_date
				        	        coverage_list.append([cov_PD[0],cov_name,VIN,policy_no, coverage_status, start_date, end_date, upadate_date])

						#select optional random coverage and random limit
					        else:
							cov_name = random.choice(["Uninsured", "Underinsured", "Medical Payments"])
	            					cov_other = random.choice(reader_coverage_data[reader_coverage_data['coverage'] == cov_name].values.tolist())

							if status == "Cancelled":
								coverage_status = "Inactive"
								coverage_list.append([cov_other[0],cov_name,VIN,policy_no, coverage_status, start_date, end_date, upadate_date])

							else:
		            					end_date = str(numpy.random.choice([current_policy[random.randint(0,len(current_policy)-1)][2],""],p=[0.4,0.6]))	    				

								if end_date == "":
									coverage_status = "Active"

								else:
									coverage_status = "Inactive"

								coverage_list.append([cov_other[0],cov_name,VIN,policy_no, coverage_status, start_date, end_date, upadate_date])

		        			j = j + 1
				k = k + 1

		    	i = i + 1
	
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	gen = time.time()
	print("Generate: "+str(gen-start))
	
	#Truncate table if already exists
	if engine.dialect.has_table(engine, CConf.c_table_name):
		logging.debug("Table "+CConf.c_table_name+" already exists!")
		tt.truncate(CConf.c_table_name)
	
	try:
		#Create table with the specified columns
		df = pd.DataFrame.from_records(coverage_list, columns=CConf.c_headers)

		#Convert to datetime
		df["record_start_date"] =  pd.to_datetime(df["record_start_date"])
		df["record_end_date"] =  pd.to_datetime(df["record_end_date"])
		df["record_update_date"] =  pd.to_datetime(df["record_update_date"])

		#load to database
		df.to_sql(CConf.c_table_name, engine, index=False)
		logging.debug("Table "+CConf.c_table_name+" created and "+str(len(coverage_list))+" records written.")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print(str(len(coverage_list))+" records written to DB in "+str(time.time()-gen))
	
def main():
	cl.generate_coverage_list()
	generate_coverage()

if __name__ == "__main__":
	main()
