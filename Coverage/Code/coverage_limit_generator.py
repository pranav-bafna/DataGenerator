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

def generate_coverage_list():
	prefix = '0'
	coverage_list = []
	i = 0
	k = 1

	while(i < len(CConf.coverage_names)):
	    j = 0
	    while(j < len(CConf.Coverage_limits)):
	        val=6-len(str(k))
	        coverage_id = "COV01-1"+prefix*val+str(k)
	        coverage_list.append([coverage_id, CConf.coverage_names[i], CConf.Coverage_limits[j]])
	        j = j + 1
		k = k + 1

	    i = i + 1
	
	#Connect to postgres
	engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')

	#Truncate the table if exists
	if engine.dialect.has_table(engine, CConf.cl_table_name):
		tt.truncate(CConf.cl_table_name)

	#Create table with the specified columns
	df = pd.DataFrame.from_records(coverage_list, columns=CConf.cl_headers)
	
	#load to database
	df.to_sql(CConf.cl_table_name, engine, index=False)

	print(str(len(coverage_list))+" Coverage Limits Generated and Loaded to DB.")


def main():
	generate_coverage_list()

if __name__ == "__main__":
	main()