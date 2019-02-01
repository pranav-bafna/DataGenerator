import csv
import random
import numpy
import uuid
import sys
import time
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

def Generate():

	i = 0
	vin_data = []
	data_list = []

	#Load expensive cars data
	reader_expcars = csv.reader(open(DGconf.expcar_file_path))
	expcar_data = list(reader_expcars)

	#Load other cars data
	reader_othercars = csv.reader(open(DGconf.othercar_file_path))
	othercar_data = list(reader_othercars)

	#load VIN data
	reader2 = csv.reader(open(DGconf.VIN_file_path))
	vin_data = list(reader2)
	
	start = time.time()
	
	while (i < DGconf.num_records):
		#Make a probability based random choice for car
		file_data = numpy.random.choice([expcar_data, othercar_data], p = DGconf.car_distribution)

		#Choose random car from the list
		chosen_car = random.choice(file_data)

		#Choose unique VIN
		chosen_row = vin_data[i+1]
		data_list.append([chosen_row[0], chosen_row[1], chosen_car[1], chosen_car[2], chosen_car[0], random.randint(35000,99999), random.randint(1,10), random.randint(8,18)])
		i = i+1

	gen = time.time()
	print("Generation: "+str(gen-start))
	print(str(i)+" Records processed!")

	#Connect to postgres
	engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')

	#Truncate if table exists
	if engine.dialect.has_table(engine, DGconf.output_table_name):
		tt.truncate(DGconf.output_table_name)

	#Create table with specified columns
	df = pd.DataFrame.from_records(data_list, columns=DGconf.headers)

	#Load to database
	df.to_sql(DGconf.output_table_name, engine, index=False)

	print("Write: "+str(time.time()-gen))
	print(str(len(data_list))+" Records written!")
	

def main():
	ds.split()
	Generate()
	
if __name__ == "__main__":
	main()
