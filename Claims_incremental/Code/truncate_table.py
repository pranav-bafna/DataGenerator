import os
import time
import logging
import traceback

if not os.path.exists(r'../logs'):
	os.makedirs(r'../logs')

timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
log_file = "../logs/truncate_" + timestamp + ".log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

try:
	from sqlalchemy import create_engine, text
	import sys

	#Importing configuration file
	sys.path.insert(0, "../Config")
	import Config_claim_il as CConf

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

def truncate(table_name):
	try:
		engine = create_engine(CConf.connection_string)
		connection = engine.connect()
		truncate_query = text("DROP TABLE "+table_name)
		connection.execution_options(autocommit=True).execute(truncate_query)
		logging.debug("Table "+table_name+" truncated.")
	
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()


#truncate(table_name)