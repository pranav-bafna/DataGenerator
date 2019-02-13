import os
import time
import logging
import traceback

if not os.path.exists(r'../logs'):
	os.makedirs(r'../logs')

timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
log_file = "../logs/claim_il_generator_" + timestamp + ".log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.debug("claims incremental data generation is started.")

try:
	#import required packages
	import csv
	import sys
	import time
	import numpy
	import random
	import psycopg2
	import pandas as pd
	from faker import Faker
	from sqlalchemy import create_engine, text
	from datetime import datetime, date, timedelta

	#Import file truncate
	import truncate_table as tt

	#Import configuration file
	sys.path.insert(0, "../Config")
	import Config_claim_il as CConf

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

fake = Faker()

try:
	engine = create_engine(CConf.connection_string)
	db_connection = engine.connect()
	logging.debug("Connected to: "+CConf.connection_string)

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

try:
	#Load Incident incremetnal table
	select = text("SELECT * FROM incident_il")
	result = db_connection.execute(select)
	reader_incident_data = pd.DataFrame(list(result), columns = result.keys())
	incident_list = reader_incident_data['incident_id'].unique().tolist()
	VIN_list = reader_incident_data['incident_vin'].unique().tolist()
	num_rec = len(VIN_list)

	#Load claims adjuster table
	select = text("SELECT * FROM claims_adjuster")
	result = db_connection.execute(select)
	adjuster_id = pd.DataFrame(list(result), columns = result.keys())['cont_id'].unique().tolist()

	#Load coverage table
	select = text("SELECT * FROM coverage")
	result = db_connection.execute(select)
	reader_coverage_data = pd.DataFrame(list(result), columns = result.keys())

	#Load claims table
	select = text("SELECT * FROM cc_claims")
	result = db_connection.execute(select)
	intermediate_data = pd.DataFrame(list(result), columns = result.keys())
	reader_claim_data = intermediate_data.values.tolist()
	claim_id_list = intermediate_data['claim_claimnumber'].values.tolist()

	#Get latest claim number
	last_id = int(str(claim_id_list[len(claim_id_list)-1]).split("IA01-1")[1]) + 1

	#Load claim resolutions to list
	resolution_list = []
	f = open(CConf.resolution_claim_file, "r")
	resolution_list = [x.strip() for x in f.readlines()] 
	f.close()

	#Load claim exposures to list
	reader = csv.reader(open(CConf.claim_primary_exposure_file))
	exposure_list = list(reader)

	#Load group types to list
	group_type_list = []
	f = open(CConf.group_type_file, "r")
	group_type_list = [x.strip() for x in f.readlines()] 
	f.close()

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()

claim_list = []
old_rec = 0

def update_existing():
	global claim_list, old_rec
	i = 0
	strt1 = time.time()

	try:
		while(i < len(reader_claim_data)):
			#Get open claims
			if (reader_claim_data[i][6] != "Closed"):

				#Check if the exposure is glass or any other
				if (reader_claim_data[i][8] == "GLASS"):
					lower_limit = reader_claim_data[i][5] + timedelta(days=15)
					upper_limit = reader_claim_data[i][5] + timedelta(days=20)
				
					if datetime.now() > lower_limit and datetime.now() < upper_limit:
						claim_status = "Closed"
						claim_closedate = str(datetime.now())
					else:
						claim_status = reader_claim_data[i][6]
						claim_closedate = reader_claim_data[i][7]
					
				#For other exposures		
				else:
					lower_limit = reader_claim_data[i][5] + timedelta(days=35)
					upper_limit = reader_claim_data[i][5] + timedelta(days=60)
				
					if datetime.now() > lower_limit and datetime.now() < upper_limit:
						claim_status = "Closed"
						claim_closedate = str(datetime.now())
					else:
						claim_status = reader_claim_data[i][6]
						claim_closedate = reader_claim_data[i][7]

				#Get rest of the claim data
				claim_id = reader_claim_data[i][0]
				claim_claimnumber = reader_claim_data[i][1]
				policy_number = reader_claim_data[i][2]
				incident_id = reader_claim_data[i][3]
				claim_lossdate = reader_claim_data[i][4]
				claim_reporteddate = reader_claim_data[i][5]
				#claim_status = reader_claim_data[i][]
				#claim_closedate= reader_claim_data[i][]
				claim_losstype = reader_claim_data[i][8]
				claim_lob = reader_claim_data[i][9]
				claim_severity = reader_claim_data[i][10]
				claim_loss_add_state = reader_claim_data[i][11]
				claim_glass_ind = reader_claim_data[i][12]
				claim_primary_group = reader_claim_data[i][13]
				claim_primary_adjuster_id = reader_claim_data[i][14]
				claim_litigation_ind = reader_claim_data[i][15]
				claim_subrogation_status = reader_claim_data[i][16]
				claim_salvage_status = reader_claim_data[i][17]
				claim_litigation_status = reader_claim_data[i][18]
				claim_fatalities = reader_claim_data[i][19]
				claim_large_loss = reader_claim_data[i][20]
				claim_coverage_in_question = reader_claim_data[i][21]
				claim_siu_status = reader_claim_data[i][22]
				claim_siu_score = reader_claim_data[i][23]
	
				#Populate claim resolution if claim is closed
				if claim_status == "Closed" and claim_siu_status == "Assigned":
					claim_resolution = "Reported in siu"

				elif claim_status == "Closed":
					claim_resolution = random.choice(resolution_list)

				else:
					claim_resolution = ""

				#claim_resolution = claim_resolution = random.choice(resolution_list)
				claim_list.append([claim_id, claim_claimnumber, policy_number, incident_id, claim_lossdate, claim_reporteddate, claim_status, claim_closedate, claim_losstype, claim_lob, claim_severity, claim_loss_add_state, claim_glass_ind, claim_primary_group, claim_primary_adjuster_id, claim_litigation_ind, claim_subrogation_status, claim_salvage_status, claim_litigation_status, claim_fatalities, claim_large_loss, claim_coverage_in_question, claim_siu_status, claim_siu_score, claim_resolution])

			i = i + 1

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print("Time1: "+str(time.time()-strt1)+" LEN: "+str(len(claim_list)))
	old_rec = len(claim_list)
	logging.debug(str(old_rec)+" records updated from history table.")


def add_new_claims():
	global num_rec, claim_list, last_id, exposure_list, old_rec
	strt2 = time.time()
	i = 0
	_id = '0'

	try:
		while(i < num_rec):    
			#Generate claim number
		        val=6-len(str(i))
		        claim_number = "IA01-1"+_id*val+str(last_id)
			claim_claim_id = "CLM01-1"+_id*val+str(last_id)

			incident_id = incident_list[i]
			VIN = reader_incident_data[reader_incident_data['incident_id'] == incident_id]['incident_vin'].values.tolist()[0]
			policy_id = reader_coverage_data[reader_coverage_data['vin'] == VIN]['policy_number'].values.tolist()[0]
			
		        date_reported = datetime.now()
		        date_start = date_reported + timedelta(days=-random.randint(0,5))
			date_closed = ""
		
		        #Generating primary exposure
		        exposure = random.choice(exposure_list)
		        expo = exposure[0]
    
		        claim_status = "Open"
			
		        #generating claim_glass_indicator
		        if (exposure[0] == "GLASS"):
			        claim_glass_ind = "Y"
			
		        else:
			        claim_glass_ind = ""
    
		        claim_litigation_ind=['']

		        if (exposure[0] == "BI"):
			        claim_litigation_ind = numpy.random.choice(list(CConf.litigation_ind.keys()),1, p = list(CConf.litigation_ind.values()))
			
		        claim_lob = "AUTO"
		
		        #generating state
		        state = fake.state_abbr()
		
		        claim_subrogation_status=''
		        if expo in ('COMP','COL'):
			        claim_subrogation_status = "Y"
        
		        claim_salvage_status=''
		        if expo in ('COMP','COL'):
			        claim_salvage_status = "Y"        
        
		        claim_fatalities=numpy.random.choice(list(CConf.fatalities.keys()),1, p = list(CConf.fatalities.values()))
		
		        claim_large_loss=numpy.random.choice(list(CConf.large_loss.keys()),1, p = list(CConf.large_loss.values()))
        
			claim_coverage_in_question=numpy.random.choice(list(CConf.coverage_in_quest.keys()),1, p = list(CConf.coverage_in_quest.values()))
        
			claim_siu_status=numpy.random.choice(list(CConf.claim_siu_status.keys()), 1, p = list(CConf.claim_siu_status.values()) )
        
			if claim_siu_status=="Assigned":
			        claim_siu_score=str(random.randint(CConf.min_siu_score,CConf.max_siu_score))
			
		        else:
			        claim_siu_score=''
			
		        claim_primary_group = random.choice(group_type_list)
		
		        claim_litigation_status = numpy.random.choice(list(CConf.claim_litigation_status.keys()),1, p = list(CConf.claim_litigation_status.values()))
		
		        claim_resolution = ""
        
			claim_primary_adjuster_id = random.choice(adjuster_id)
    
		        claim_list.append([claim_claim_id, claim_number, policy_id, incident_id, date_start, date_reported, claim_status, date_closed, exposure[0], claim_lob, exposure[1], state,claim_glass_ind, claim_primary_group, claim_primary_adjuster_id, claim_litigation_ind[0], claim_subrogation_status, claim_salvage_status, claim_litigation_status[0], claim_fatalities[0], claim_large_loss[0], claim_coverage_in_question[0], claim_siu_status[0], claim_siu_score, claim_resolution])
        
		        i = i + 1
			last_id = last_id + 1
	
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print("Time2: "+str(time.time()-strt2))
	
	#Truncate table if already exists
	if engine.dialect.has_table(engine, CConf.claim_il_table):
		logging.debug("Table "+CConf.claim_il_table+" already exists!")
		tt.truncate(CConf.claim_il_table)

	wrt = time.time()
	
	try:
		#Create table with the specified columns
		df = pd.DataFrame.from_records(claim_list, columns=CConf.claim_headers)

		#Convert date to datetime
		df["claim_lossdate"] =  pd.to_datetime(df["claim_lossdate"])
		df["claim_reporteddate"] =  pd.to_datetime(df["claim_reporteddate"])
		df["claim_closedate"] =  pd.to_datetime(df["claim_closedate"])
	
		#load to database
		df.to_sql(CConf.claim_il_table, engine, index=False)
		new_rec = len(claim_list) - old_rec
		logging.debug(str(new_rec)+" records created.")
		logging.debug("Table "+CConf.claim_il_table+" created and "+str(len(claim_list))+" total records written.")

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print(str(len(claim_list))+" records written to DB in "+str(time.time()-wrt))    

def main():
	strt = time.time()
	update_existing()
	add_new_claims()
	gen = time.time()
	print("Total: "+str(gen-strt))

if __name__ == "__main__":
	main()
