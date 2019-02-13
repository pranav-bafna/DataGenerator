####################################################################
try:
	import os
	import logging
	import time
	import traceback
	if not os.path.exists(r'../logs'):
		os.makedirs(r'../logs')

	timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
	log_file = "../logs/table_to_csv_log_" + timestamp + ".log"
	logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
	logging.debug("Table to csv script started executing for all tables")
except Exception,e:
	print str(e)

####################################################################

# Import all required modules

try:
	from sqlalchemy import create_engine, text
	import pandas as pd
	import sys
	sys.path.insert(0, '../configuration')
	import database_credentials as dc
	import tables_to_csv_config as tcc

except Exception,e:
	print str(e)
	logging.debug(traceback.format_exc())
	exit()

logging.debug("Successfully imported all the required modules")

############################# MAIN #############################
def main():

	try:
		engine = create_engine(dc.connection_string)
		connection = engine.connect()

		logging.debug("Connetion to the postgres database is successful")
		table_names = engine.table_names()
	except Exception,e:
		print "Error Connection issue..."
		logging.debug(traceback.format_exc())
		logging.debug("Error: " + str(e))	
		exit()

	try:	
		for table in table_names:
			path = tcc.output_path + table + ".csv"
			print path 
			data_q = text("select * from "+table)
			data = connection.execute(data_q).fetchall()
			headers = connection.execute(data_q).keys()
			df = pd.DataFrame(data,columns = headers)
			df.to_csv(path, index = False, encoding = 'utf-8')
			logging.debug("Table " + str(table) + " successfully converted into csv file")
	except Exception,e:
		print "Error in converting tables to csv..."
		logging.debug(traceback.format_exc())
		logging.debug("Error: " + str(e))	
		exit()
	

if __name__=="__main__":
	main()	
