import os
import time
import logging
import traceback

if not os.path.exists(r'../logs'):
	os.makedirs(r'../logs')

timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
log_file = "../logs/incident_data_generator_" + timestamp + ".log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.debug("Incident data generation is started.")

try:
	import csv
	import time
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
	import Config_incident as Iconf

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

def generate_incidents():
	i=1
	id = '0'
	VIN_list = []
	incident_list = []
	relations = ["Self", "Spouse", "Brother", "Sister", "Mother", "Father", "Son", "Daughter", "Third Party"]

	try:
		#Connect to postgres
		engine = create_engine(Iconf.connection_string)
		db_connection = engine.connect()
		logging.debug("Connected to: "+Iconf.connection_string)

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	try:
		#Load coverage table
		select = text("SELECT * FROM coverage")
		result = db_connection.execute(select)
		reader_coverage_data = pd.DataFrame(list(result), columns = result.keys())
		VIN_list = reader_coverage_data[reader_coverage_data['coverage_status'] == 'Active']['vin'].unique().tolist()
		num_rec = random.randint(len(VIN_list)-20000, len(VIN_list))

		#Load incident descriptions
		reader = csv.reader(open(Iconf.inc_des_path))
		incident_desc_list = list(reader)
		logging.debug("Data loaded.")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	start = time.time()

	try:
		while(i <= num_rec):
		    val=5-len(str(i))
		    inc_incident_id = "INC01-1"+id*val+str(i)
		    value = random.randint(0,len(VIN_list))

		    if value == len(VIN_list):
			value = value - 1

		    inc_vehicle_id = VIN_list[value] 
		    VIN_list.pop(value)

		    incident_desc = random.choice(incident_desc_list)

		    driver = random.choice(relations)

		    inc_is_the_vehicle_driveable = numpy.random.choice(["Y",""],p = [0.8,0.2])

		    incident_list.append([inc_incident_id, inc_vehicle_id, incident_desc[0], driver, inc_is_the_vehicle_driveable])

		    i = i + 1

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print("Generate: "+str(time.time()-start))

	#Truncate table if exists
	if engine.dialect.has_table(engine, Iconf.table_name):
		logging.debug("Table "+Iconf.table_name+" already exists!")
		tt.truncate(Iconf.table_name)

	try:
		#Create table with the specified columns
		df = pd.DataFrame.from_records(incident_list, columns=Iconf.headers)

		#Load to database
		df.to_sql(Iconf.table_name, engine, index=False)
		logging.debug(Iconf.table_name+" created and "+str(len(incident_list))+" records written.")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()
	
	print(str(i)+" Records Generated and loaded to DB!")

def main():
	generate_incidents()
	
if __name__ == "__main__":
	main()