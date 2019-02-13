import os
import time
import logging
import traceback

if not os.path.exists(r'../logs'):
	os.makedirs(r'../logs')

timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
log_file = "../logs/claim_data_generator_" + timestamp + ".log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.debug("Claims data generation is started.")

try:
	#import required packages
	from faker import Faker
	import random
	from datetime import datetime, date, timedelta
	import numpy
	import csv
	import pandas as pd
	from sqlalchemy import create_engine, text
	import psycopg2

	# Import sys to import config python files
	import sys
	sys.path.insert(0, '../configuration')
	import claims_config as cc

	#Import file truncate
	import truncate_table as tt

except Exception,e:
	print(str(e))
	logging.info(traceback.format_exc())
	exit()

fake = Faker()

try:
	engine = create_engine(cc.connection_string)
	db_connection = engine.connect()
	logging.debug("Connected to: "+cc.connection_string)

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

try:
	#Load coverage table
	select = text("SELECT * FROM incidents")
	result = db_connection.execute(select)
	reader_incident_data = pd.DataFrame(list(result), columns = result.keys())
	incident_list = reader_incident_data['incident_id'].unique().tolist()
	VIN_list = reader_incident_data['incident_vin'].unique().tolist()
	num_rec = len(VIN_list)

	select = text("SELECT * FROM claims_adjuster")
	result = db_connection.execute(select)
	adjuster_id = pd.DataFrame(list(result), columns = result.keys())['cont_id'].unique().tolist()

	select = text("SELECT * FROM coverage")
	result = db_connection.execute(select)
	reader_coverage_data = pd.DataFrame(list(result), columns = result.keys())

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()
	
def generate_claims():
	exposure_list = []
	data = []
	claim_data = []
	claim_list = []
	i = 0
	_id = '0'

	
    	try:
		#Load exposures
		reader = csv.reader(open(cc.claim_primary_exposure_file))
		exposure_list = list(reader)
	
		#Load group types
		group_type_list = []
		f = open(cc.group_type_file, "r")
		group_type_list = [x.strip() for x in f.readlines()]
		f.close()
	
		#Load resolutions
		resolution_list = []
		f = open(cc.resolution_claim_file, "r")
		resolution_list = [x.strip() for x in f.readlines()]
		f.close()
		logging.debug("Data loaded.")
	
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()
	
	
	strt = time.time()

	try:
		while i < num_rec:
		        #generating claim number of same length
		        val=6-len(str(i))
		        claim_number = "IA01-1"+_id*val+str(i)
		
			claim_claim_id = "CLM01-1"+_id*val+str(i)

			incident_id = incident_list[i]
	
			VIN = reader_incident_data[reader_incident_data['incident_id'] == incident_id]['incident_vin'].values.tolist()[0]
	
			policy_id = reader_coverage_data[reader_coverage_data['vin'] == VIN]['policy_number'].values.tolist()[0]
		
		        #Generating date between given dates
		        start = fake.date_time_between_dates(datetime_start=cc.claim_start_date, datetime_end=cc.claim_end_date, tzinfo=None)
		
		        #generating Report_date and loss_date (with difference of 5 days)
		        days_reported = random.randint(0,cc.reported_days)
		        reported = start + timedelta(days=days_reported)
		        date_start = str(start).split()[0]
		        date_reported = str(reported).split()[0]
		
		        #Generating primary exposure
		        exposure = random.choice(exposure_list)
		        expo = exposure[0]
    
		        #Generating exposure status based on date using probability between open and close
		        if start > cc.exp_start_date and start < cc.exp_end_date:
			        exp_status = numpy.random.choice(list(cc.exp_status_within_dates.keys()), 1, p = list(cc.exp_status_within_dates.values()))
		        else:
			        exp_status = numpy.random.choice(list(cc.exp_status_outside_dates.keys()), 1, p = list(cc.exp_status_outside_dates.values()))
			
		        #Condition to generate closed_date    
		        if (exp_status == "Closed" and exposure[0] == "GLASS"):
			        end = start + timedelta(days=random.randint(cc.min_glass_close_days, cc.max_glass_close_days))
			        date_closed = str(end).split()[0]
			
		        	if end > cc.exp_close_date:
			                exp_status = ["Open"]
			                date_closed = ""
				
		        elif (exp_status == "Closed" and exposure[0] != "GLASS"):
			        end = start + timedelta(days=random.randint(cc.min_other_close_days, cc.max_other_close_days))
			        date_closed = str(end).split()[0]
			
			        if end > cc.exp_close_date:
			                exp_status = ["Open"]
			                date_closed = ""
	        	else:    
			        date_closed = ""
			
		        #generating claim_glass_indicator
		        if (exposure[0] == "GLASS"):
			        claim_glass_ind = "Y"
			
		        else:
			        claim_glass_ind = ""
    
		        claim_litigation_ind=['']  
		        if (exposure[0] == "BI"):
			        claim_litigation_ind = numpy.random.choice(list(cc.litigation_ind.keys()),1, p = list(cc.litigation_ind.values()))
			
		        claim_lob = "AUTO"
		
		        #generating state
		        state = fake.state_abbr()
		
		        claim_subrogation_status=''
		        if expo in ('COMP','COL'):
			        claim_subrogation_status = "Y"
        
		        claim_salvage_status=''
		        if expo in ('COMP','COL'):
			        claim_salvage_status = "Y"        
        
		        claim_fatalities=numpy.random.choice(list(cc.fatalities.keys()),1, p = list(cc.fatalities.values()))
		
		        claim_large_loss=numpy.random.choice(list(cc.large_loss.keys()),1, p = list(cc.large_loss.values()))
        
			claim_coverage_in_question=numpy.random.choice(list(cc.coverage_in_quest.keys()),1, p = list(cc.coverage_in_quest.values()))
        
			claim_siu_status=numpy.random.choice(list(cc.claim_siu_status.keys()), 1, p = list(cc.claim_siu_status.values()) )
        
			if claim_siu_status=="Assigned":
			        claim_siu_score=str(random.randint(cc.min_siu_score,cc.max_siu_score))
			
		        else:
			        claim_siu_score=''
			
		        claim_primary_group = random.choice(group_type_list)
		
		        claim_litigation_status = numpy.random.choice(list(cc.claim_litigation_status.keys()),1, p = list(cc.claim_litigation_status.values()))
	
			if exp_status == "Closed" and claim_siu_status == "Assigned":
				claim_resolution = "Reported in siu"

			elif exp_status == "Closed":
				claim_resolution = random.choice(resolution_list)
		
			else:
				claim_resolution = ""
        
			claim_primary_adjuster_id = random.choice(adjuster_id)
    
		        #Generate one row
		        data = [claim_claim_id, claim_number, policy_id, incident_id, date_start, date_reported, str(exp_status[0]), date_closed, exposure[0], claim_lob, exposure[1], state,claim_glass_ind, claim_primary_group, claim_primary_adjuster_id, claim_litigation_ind[0], claim_subrogation_status, claim_salvage_status, claim_litigation_status[0], claim_fatalities[0], claim_large_loss[0], claim_coverage_in_question[0], claim_siu_status[0], claim_siu_score, claim_resolution]
		        claim_list.append(data)
		        i = i + 1

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()
    
	gen = time.time()
	print("Generate: "+str(gen-strt))
	
	#Truncate table if already exists
	if engine.dialect.has_table(engine, cc.claim_table_name):
		logging.debug("Table "+cc.claim_table_name+" already exists!")
		tt.truncate(cc.claim_table_name)
	
	try:
		#Create table with the specified columns
		df = pd.DataFrame.from_records(claim_list, columns=cc.claim_headers)

		#Convert date to datetime
		df["claim_lossdate"] =  pd.to_datetime(df["claim_lossdate"])
		df["claim_reporteddate"] =  pd.to_datetime(df["claim_reporteddate"])
		df["claim_closedate"] =  pd.to_datetime(df["claim_closedate"])
	
		#load to database
		df.to_sql(cc.claim_table_name, engine, index=False)
		logging.debug(cc.claim_table_name+" created and "+str(len(claim_list))+" records written.")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print(str(len(claim_list))+" records written to DB in "+str(time.time()-gen))

generate_claims()