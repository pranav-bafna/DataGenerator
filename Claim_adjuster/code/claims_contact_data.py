###########################################################
try:
	import os
	import logging
	import time
	import traceback
	if not os.path.exists(r'../logs'):
		os.makedirs(r'../logs')


	timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
	log_file = "../logs/claim_ajuster_log_" + timestamp + ".log"
	logging.basicConfig(filename=log_file,level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
	logging.info("Generation of claim adjuster data script started executing...")
except Exception,e:
	print str(e)

###############################################################


# Import all required modules
try:
	import faker
	import csv
	import random
	import numpy
	from datetime import datetime
	import uuid

	import pandas as pd
	from sqlalchemy import create_engine
	import psycopg2

	import sys
	sys.path.insert(0, '../configuration')
	import claim_contact_config as ccc
	import database_credentials as dc

	import logging
except Exception,e:
	print str(e)
	logging.info(traceback.format_exc())
	exit()

logging.info("Successfully imported all the required modules")
fake = faker.Faker("en_US")

######################## GET MAIL ID'S #############################
# Function to get the mail id's
def get_email_id(family_member_name,family_last_name):
	
	random_domain = random.choice(ccc.email_domains)
	email_format = numpy.random.choice([1,2,3],p=[0.34,0.34,0.32])

	try:
		if email_format == 1:
			family_member_email = family_member_name.lower() + "." + family_last_name.lower() + "@" +random_domain + ".com"
		elif email_format == 2:
			family_member_email = family_member_name.lower()[0] + family_last_name.lower() + str(random.randrange(100,999)) + "@" +random_domain + ".com"
		elif email_format == 3:
			family_member_email = family_last_name.lower() + family_member_name.lower()[0] + str(random.randrange(10,999)) + "@" +random_domain + ".com"
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()
	
	return family_member_email


############################# GET DOB #############################
# Function to get DOB
def get_dob():
	year = (random.randint(ccc.dob_min_year,ccc.dob_max_year))
	month = random.choice(range(1,13))

	try:
	    	if month == 2:
        		day = random.choice(range(1, 29))
	    	else:
        		day = random.choice(range(1, 31))

		birth_date = datetime(year, month, day).isoformat().strip().split("T")[0]
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	return birth_date

############################# MAIN #############################
def main():
	logging.info("In main function")
	headers = ccc.headers
	final_data = []

	print "***********Getting data*************"
	
	try:
		logging.info("Reading unique ID csv to get unique contact id's")
		contactid_data = csv.reader(open(ccc.unique_id_file))
		contactid_data.next()
		id_data = list(contactid_data)
		logging.info("Read unique ID file successfully")
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()
	
	try:
		# Iterate loop for number of claims contacts
		for i in range(0,ccc.count):
			# get contact ID
			cont_id = id_data[i][6]

			# get name
			first_name = fake.first_name()
			last_name = fake.last_name()
			name = first_name + " " + last_name
		
			# get phone number
			phone_no = "+1-"+str(random.randrange(100,999))+"-"+str(random.randrange(100,999))+"-"+str(random.randrange(1000,9999))

			# get address
			address = fake.address().replace('\n',' ') + ", US"

			# get email address
			email_address = get_email_id(first_name, last_name)

			# get dob
			birth_date = get_dob()

			final_data.append([cont_id, name, address, phone_no, email_address, birth_date])

		logging.info("Successfully generated required claims adjuster data")
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	try:
		df = pd.DataFrame.from_records(final_data, columns=headers)
		df.reset_index()

		df["cont_dateofbirth"] =  pd.to_datetime(df["cont_dateofbirth"])
		df["cont_dateofbirth"] = df["cont_dateofbirth"].dt.date
	
		engine = create_engine(dc.connection_string)
		df.to_sql(ccc.table_name, engine, index=False)
		logging.info("Successfully loaded "+ str(ccc.count) + " claims adjuster records in postgres")
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()


if __name__=="__main__":
	main()	
	