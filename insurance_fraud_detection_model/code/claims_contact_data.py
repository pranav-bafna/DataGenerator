# Import all required modules
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


fake = faker.Faker("en_US")

######################## GET MAIL ID'S #############################
# Function to get the mail id's
def get_email_id(family_member_name,family_last_name):
	random_domain = random.choice(["yahoo","gmail","outlook","hotmail"])
	
	email_format = numpy.random.choice([1,2,3],p=[0.34,0.34,0.32])
	if email_format == 1:
		family_member_email = family_member_name.lower() + "." + family_last_name.lower() + "@" +random_domain + ".com"
	elif email_format == 2:
		family_member_email = family_member_name.lower()[0] + family_last_name.lower() + str(random.randrange(100,999)) + "@" +random_domain + ".com"
	elif email_format == 3:
		family_member_email = family_last_name.lower() + family_member_name.lower()[0] + str(random.randrange(10,999)) + "@" +random_domain + ".com"
	
	return family_member_email


############################# GET DOB #############################
# Function to get DOB
def get_dob():
	year = (random.randint(ccc.dob_min_year,ccc.dob_max_year))
	month = random.choice(range(1,13))
    	if month == 2:
        	day = random.choice(range(1, 29))
    	else:
        	day = random.choice(range(1, 31))

	birth_date = datetime(year, month, day).isoformat().strip().split("T")[0]

	return birth_date

############################# MAIN #############################
def main():
	headers = ccc.headers
	final_data = []

	print "***********Getting data*************"
	
	contactid_data = csv.reader(open(ccc.unique_id_file))
	contactid_data.next()
	id_data = list(contactid_data)

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

	df = pd.DataFrame.from_records(final_data, columns=headers)
	df.reset_index()

	df["cont_dateofbirth"] =  pd.to_datetime(df["cont_dateofbirth"])
	df["cont_dateofbirth"] = df["cont_dateofbirth"].dt.date
	
	engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')
	df.to_sql(table_name, engine)

	
if __name__=="__main__":
	main()	
	