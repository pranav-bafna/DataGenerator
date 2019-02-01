# Import all required modules
import csv
import uuid
import random

import pandas as pd
from sqlalchemy import create_engine
import psycopg2

import sys
sys.path.insert(0, '../configuration')

import claim_finance_config as cfc

############################# MAIN #############################
def main():

	final_data = []

	input_data = pd.read_csv(cfc.exp_file,usecols=["exposure_id","exp_claim_id"]).values.tolist()
	headers = cfc.headers

	id_data = csv.reader(open(cfc.unique_id_file))
	id_data.next()
	id_data_lst = list(id_data)

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

	df = pd.DataFrame.from_records(final_data, columns=headers)
	
	engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')
	df.to_sql(cfc.table_name, engine, index=False)


if __name__=="__main__":
	main()
			