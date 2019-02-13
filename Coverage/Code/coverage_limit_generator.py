import os
import time
import logging
import traceback

if not os.path.exists(r'../logs'):
	os.makedirs(r'../logs')

timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
log_file = "../logs/vehicle_data_generator_" + timestamp + ".log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.debug("Coverage limits generation is started.")

try:
	import csv
	import sys
	import random
	import psycopg2
	import pandas as pd
	from sqlalchemy import create_engine

	#Import file truncate
	import truncate_table as tt

	#Import configuration file
	sys.path.insert(0, "../Config")
	import Config_CovGen as CConf

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

def generate_coverage_list():
	prefix = '0'
	coverage_list = []
	i = 0
	k = 1

	try:
		while(i < len(CConf.coverage_names)):
		    j = 0

		    while(j < len(CConf.Coverage_limits)):
		        val=CConf.id_length-len(str(k))
		        coverage_id = CConf.cov_id_prefix+prefix*val+str(k)

		        coverage_list.append([coverage_id, CConf.coverage_names[i], CConf.Coverage_limits[j]])

	        	j = j + 1

			k = k + 1

		    i = i + 1

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	try:
		#Connect to postgres
		engine = create_engine(CConf.connection_string)
		logging.debug("Connected to: "+CConf.connection_string)

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	#Truncate the table if exists
	if engine.dialect.has_table(engine, CConf.cl_table_name):
		logging.debug("Table "+CConf.cl_table_name+" already exists!")
		tt.truncate(CConf.cl_table_name)

	try:
		#Create table with the specified columns
		df = pd.DataFrame.from_records(coverage_list, columns=CConf.cl_headers)
	
		#load to database
		df.to_sql(CConf.cl_table_name, engine, index=False)
		logging.debug(CConf.cl_table_name+" created and "+str(len(coverage_list))+" records written.")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print(str(len(coverage_list))+" Coverage Limits Generated and Loaded to DB.")


def main():
	generate_coverage_list()

if __name__ == "__main__":
	main()