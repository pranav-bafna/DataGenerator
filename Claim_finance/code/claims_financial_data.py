####################################################################
try:
	import os
	import logging
	import time
	import traceback
	if not os.path.exists(r'../logs'):
		os.makedirs(r'../logs')

	timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
	log_file = "../logs/claims_finance_log_" + timestamp + ".log"
	logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
	logging.debug("Generation of claim finance data script started executing...")
except Exception,e:
	print str(e)

####################################################################

try:
	# Import all required modules
	import csv
	import uuid
	import random

	import pandas as pd
	from sqlalchemy import create_engine, text
	import psycopg2

	import sys
	sys.path.insert(0, '../configuration')
	import database_credentials as dc

	import claim_finance_config as cfc
except Exception,e:
	print str(e)
	logging.debug(traceback.format_exc())
	exit()
logging.debug("Successfully imported all the required modules")

############################# MAIN #############################
def main():

	final_data = []

	#input_data = pd.read_csv(cfc.exp_file,usecols=["exposure_id","exp_claim_id"]).values.tolist()
	try:
		logging.debug("Connecting to postgres")
		#connect to postgres
		engine = create_engine(dc.connection_string)
		db_connection = engine.connect()
		logging.debug("Connection to the postgres succeeded")
	except Exception,e:
		print "Error Connection issue..."
		logging.debug(traceback.format_exc())
		logging.debug("Error: " + str(e))	
		exit()

	try:
		logging.debug("Reading exposure table from postgres")
		#read exposure table from database
		select = text("select * from " + cfc.exposure_table)
		result = db_connection.execute(select)
		input_data = pd.DataFrame(list(result), columns = result.keys())
	except Exception,e:
		print "Error in getting data from table"
		logging.debug(traceback.format_exc())
		logging.debug("Error: " + str(e))
		exit()

	input_data = input_data.filter(items=["exposure_id","exp_claim_id"]).values.tolist()

	headers = cfc.headers

	try:
		logging.debug("Reading unique ID csv file")
		id_data = csv.reader(open(cfc.unique_id_file))
		id_data.next()
		id_data_lst = list(id_data)
	except Exception,e:
		print str(e)
		logging.debug(traceback.format_exc())
		exit()

	try:
		logging.debug("started generating claims finance data")
		for i in range(len(input_data)):
			# get random claim ID
			claim_id = input_data[i][1]

			# get random exp ID
			exp_id = input_data[i][0]

			# get financial remaining reserves
			rem_res = random.randint(500,10000)

			# get total paid
			tot_paid = random.randint(500,10000)

			# get total recoveries
			tot_rec = random.randint(499,tot_paid)

			# get net total incurred
			tot_inc = tot_paid - tot_rec

			final_data.append([claim_id, exp_id, rem_res, tot_paid, tot_rec, tot_inc])

		logging.debug("Successfully created data for claims finance")
	except Exception,e:
		print str(e)
		logging.debug(traceback.format_exc())
		exit()

	df = pd.DataFrame.from_records(final_data, columns=headers)

	try:
		engine = create_engine(dc.connection_string)
		df.to_sql(cfc.table_name, engine, index=False)
		logging.debug("Successfully loaded " + str(len(input_data)) + " claims finance records in database")
	except Exception,e:
		print str(e)
		logging.debug(traceback.format_exc())
		exit()


if __name__=="__main__":
	main()
			