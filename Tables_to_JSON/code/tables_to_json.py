###########################################################
try:
	import os
	import logging
	import time
	import traceback
	if not os.path.exists(r'../logs'):
		os.makedirs(r'../logs')

	timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
	log_file = "../logs/tables_to_json_log_" + timestamp + ".log"
	logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
	logging.debug("Table to json script started executing")
except Exception,e:
	print str(e)

###############################################################

try:
	import pandas as pd
	from sqlalchemy import create_engine, text
	import psycopg2
	import json

	import sys
	sys.path.insert(0, '../configuration')
	import database_credentials as dc
	import tables_to_json_config as config

except Exception,e:
	print str(e)
	logging.debug(traceback.format_exc())
	exit()

logging.debug("Successfully imported all the required modules")

############################# MAIN #############################
def main():

	logging.debug("In main function")
	try:
		#connect to postgres
		engine = create_engine(dc.connection_string)
		db_connection = engine.connect()
		logging.debug("Connection to the database is successful")
	except Exception,e:
		print "Error Connection issue..."
		logging.debug(traceback.format_exc())
		logging.debug("Error: " + str(e))	
		exit()

	try:
		#read policy incremental table from database
		logging.debug("Read table that needs to be converted to the json file")
		select = text("select * from " + config.table_name)
		result = db_connection.execute(select)
		policy_data = pd.DataFrame(list(result), columns = result.keys())
	except Exception,e:
		print "Error in getting data from table"
		logging.debug(traceback.format_exc())
		logging.debug("Error: " + str(e))
		exit()

	try:
		policy_data['recordstartdate'] = policy_data['recordstartdate'].dt.round('1s')
	except Exception,e:
		print "Error in coversion of time"
		logging.debug(traceback.format_exc())

	try:
		logging.debug("Writing table data into JSON file")
		policy_data.astype(str).to_json(config.table_json_path, orient='records', lines=True, date_format='iso')
	except Exception,e:
		print "Error in writing data to json"
		logging.debug(traceback.format_exc())
		logging.debug("Error: " + str(e))
		exit()

	logging.debug("Success")

if __name__=="__main__":
	main()	
	