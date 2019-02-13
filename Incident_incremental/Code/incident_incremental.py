import os
import time
import logging
import traceback

if not os.path.exists(r'../logs'):
	os.makedirs(r'../logs')

timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
log_file = "../logs/incidnet_il_generator_" + timestamp + ".log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.debug("Incident incremental data generation is started.")

try:
	import csv
	import sys
	import numpy
	import random
	import psycopg2
	import pandas as pd
	from sqlalchemy import create_engine, text

	#Import file truncate
	import truncate_table as tt

	#Importing configuration file
	sys.path.insert(0, "../Config")
	import Config_incident_il as iconf

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

def generate_incident():
	i=1
	id = '0'
	incident_list = []
	relations = ["Self", "Spouse", "Brother", "Sister", "Mother", "Father", "Son", "Daughter", "Third Party"]

	try:
		#Connect to postgres
		engine = create_engine(iconf.connection_string)
		db_connection = engine.connect()
		logging.debug("Connected to: "+iconf.connection_string)

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	try:
		#Load coverage table
		select = text("SELECT * FROM coverage")
		result = db_connection.execute(select)
		reader_coverage_data = pd.DataFrame(list(result), columns = result.keys())
		cov_vin = reader_coverage_data[reader_coverage_data['coverage_status'] == 'Active']['vin'].unique().tolist()
		#num_rec = random.randint(len(VIN_list)-20000, len(VIN_list))

		select = text("SELECT * FROM incidents")
		result = db_connection.execute(select)
		reader_incident_data = pd.DataFrame(list(result), columns = result.keys())
		inc_vin = reader_incident_data['incident_vin'].unique().tolist()
		inc_id_list = reader_incident_data['incident_id'].unique().tolist()
		last_id = int(str(inc_id_list[len(inc_id_list)-1]).split("INC01-1")[1]) + 1

		VIN_list_1 = [value for value in cov_vin if value not in inc_vin] 

		#Load incident descriptions
		reader = csv.reader(open(iconf.inc_des_path))
		incident_desc_list = list(reader)
		logging.debug("Data loaded")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	i = 0
	start = time.time()
	num_rec = random.randint(iconf.lower_limit, iconf.upper_limit)

	try:
		while(i < num_rec):
		    val=6-len(str(last_id))
		    inc_incident_id = "INC01-1"+id*val+str(last_id)
		    rec_no = random.randint(0, len(VIN_list_1))
		    if rec_no == len(VIN_list_1):
			rec_no = rec_no - 1
		    inc_vehicle_id = VIN_list_1[rec_no]
		    VIN_list_1.pop(rec_no)
   
		    incident_desc = random.choice(incident_desc_list)

		    driver = random.choice(relations)

		    inc_is_the_vehicle_driveable = numpy.random.choice(list(iconf.vehicle_driveable_flag.keys()), p = list(iconf.vehicle_driveable_flag.values()))

		    incident_list.append([inc_incident_id, inc_vehicle_id, incident_desc[0], driver, inc_is_the_vehicle_driveable])

		    i = i + 1
		    last_id = last_id + 1

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print("Generate: "+str(time.time()-start))

	#Truncate table if exists
	if engine.dialect.has_table(engine, iconf.table_name):
		logging.debug("Table "+iconf.table_name+" already exists!")
		tt.truncate(iconf.table_name)

	try:
		#Create table with the specified columns
		df = pd.DataFrame.from_records(incident_list, columns=iconf.headers)

		#Load to database
		df.to_sql(iconf.table_name, engine, index=False)
		logging.debug("Table "+iconf.table_name+" created and "+str(len(incident_list))+" records written.")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print(str(i)+" Records Generated and loaded to DB!")

def main():
	generate_incident()
	
if __name__ == "__main__":
	main()