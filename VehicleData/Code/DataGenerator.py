import os
import time
import logging
import traceback

if not os.path.exists(r'../logs'):
	os.makedirs(r'../logs')

timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
log_file = "../logs/vehicle_data_generator_" + timestamp + ".log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.debug("Vehicle data generation is started.")

try:
	import csv
	import random
	import numpy
	import uuid
	import sys
	import psycopg2
	import pandas as pd
	from sqlalchemy import create_engine

	#Importing file splitter 
	import DataSplitter as ds

	#Import file truncate
	import truncate_table as tt

	#Importing configuration file
	sys.path.insert(0, "../Config")
	import Config_DataGenerator as DGconf

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

def Generate():

	i = 0
	vin_data = []
	data_list = []

	try:
		#Load expensive cars data
		reader_expcars = csv.reader(open(DGconf.expcar_file_path))
		expcar_data = list(reader_expcars)

		#Load other cars data
		reader_othercars = csv.reader(open(DGconf.othercar_file_path))
		othercar_data = list(reader_othercars)
		len_check = len(othercar_data)

		#load VIN data
		reader2 = csv.reader(open(DGconf.VIN_file_path))
		vin_data = list(reader2)
		logging.debug("Data imported.")
	
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()
	
	start = time.time()

	try:
		while (i < DGconf.num_records):
			#Make a probability based random choice for car
			file_data = numpy.random.choice([expcar_data, othercar_data], p = DGconf.car_distribution)

			#Decide car price depending on type of car
			if len(file_data) == len_check:
				car_price = random.randint(DGconf.min_othercar_price, DGconf.max_othercar_price)
			else:
				car_price = random.randint(DGconf.min_expcar_price, DGconf.max_expcar_price)

			#Choose random car from the list
			chosen_car = random.choice(file_data)

			#Choose a random car age
			car_age = random.randint(DGconf.min_car_age, DGconf.max_car_age)

			#Choose a random car mileage
			car_mileage = random.randint(DGconf.min_car_mileage, DGconf.max_car_mileage)

			#Choose unique VIN
			chosen_row = vin_data[i+1]

			data_list.append([chosen_row[0], chosen_row[1], chosen_car[1], chosen_car[2], chosen_car[0], car_price, car_age, car_mileage])
			i = i+1

	except Exception,e:
			print(str(e))
			logging.debug(traceback.format_exc())
			exit()

	gen = time.time()
	print("Generation: "+str(gen-start))
	print(str(i)+" Records processed!")

	try:
		#Connect to postgres
		engine = create_engine(DGconf.connection_string)
		logging.debug("Connected to: "+DGconf.connection_string) 

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	#Truncate if table exists
	if engine.dialect.has_table(engine, DGconf.output_table_name):
		logging.debug("Table "+DGconf.output_table_name+" already exists!")
		tt.truncate(DGconf.output_table_name)

	try:
		#Create table with specified columns
		df = pd.DataFrame.from_records(data_list, columns=DGconf.headers)

		#Load to database
		df.to_sql(DGconf.output_table_name, engine, index=False)
		logging.debug(DGconf.output_table_name+" table created and "+str(len(data_list))+" records written")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print("Write: "+str(time.time()-gen))
	print(str(len(data_list))+" Records written!")
	

def main():
	ds.split()
	Generate()
	
if __name__ == "__main__":
	main()
