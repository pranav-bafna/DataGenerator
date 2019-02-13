###########################################################
try:
	import os
	import logging
	import time
	import traceback
	if not os.path.exists(r'../logs'):
		os.makedirs(r'../logs')

	timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
	log_file = "../logs/customer_log_" + timestamp + ".log"
	logging.basicConfig(filename=log_file,level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
	logging.info("Generation of customer data script started executing...")
except Exception,e:
	print str(e)

###############################################################

try:
	# Import all required modules
	# Import faker to generate fake data
	import faker
	import csv
	import random
	import time   
	from multiprocessing import Pool                                                                                                                                                                                         

	# Import sys package to import config python files
	import sys
	sys.path.insert(0, '../configuration')

	# Input and Output path file present in "configuration folder"
	import input_file_paths as ifp
	import output_file_paths as ofp
	import database_credentials as dc

	import numpy
	from datetime import datetime, date
	import pandas as pd
	import psycopg2
	from sqlalchemy import create_engine, select, MetaData, Table, text
except Exception,e:
	print str(e)
	logging.info(traceback.format_exc())
	exit()

logging.info("Successfully imported all the required modules")
fake = faker.Faker("en_US")

############################ GET FIRST NAMES #################################
# function to get first name and genders of all family members

def get_first_name(gender, female_names_data, male_names_data):

	first_names_lst = []
	gender_lst = []

	try:
		# Iterate over all family members
		for gen in gender:

			# If gender female pick random name from female_names else male_names	
			if gen == "F":
				first_names_lst.append(random.choice(female_names_data).strip())
				gender_lst.append("Female")
			else:
        	        	first_names_lst.append(random.choice(male_names_data).strip())
                		gender_lst.append("Male")
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	return [first_names_lst,gender_lst]


############################## GET DOB ###############################
# function to get date of births and age of all family members

def get_dob(family_member_cnt, age_probability_data):

	# Get the year for which the data needs to be generated from config file
	dgy = ofp.data_genearation_year
	i = 0
	DOB = []
	
	try:
		# according to probabilties and age limits mentioned in config generate years
		while(1):
			year_lst = []
			prob_lst = []
			for row in age_probability_data:
				year = (random.randint((dgy - int(row["max_age"])),(dgy - int(row["min_age"]))))
				year_lst.append(year)
				prob_lst.append(row["probability"])

			num = numpy.random.choice(year_lst,family_member_cnt, replace=False, p=prob_lst)

			# If first age is greater than age 25 then break the loop
			if int(num[0]) < (dgy - 25):
				break
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()
	
	try:
		# Generate DOB's for all family members
		while(i < family_member_cnt):
    			month = random.choice(range(1,13))
	    		if month == 2:
        			day = random.choice(range(1, 29))
    			else:
        			day = random.choice(range(1, 31))
	    		birth_date = datetime(num[i], month, day).isoformat().strip().split("T")[0]
    			DOB.append(birth_date)
    			i = i+1
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	# Generate ages for all family members
	try:
		age = []
		for member in DOB: 
			age.append(int(str((datetime(dgy,1,1).date() - datetime.strptime(str(member).split()[0], '%Y-%m-%d').date())/365).split()[0]))
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	return [DOB,age]
   

############################## GET RELATIONSHIPS ############################## 
# function to get the relationships within all family members

def get_relationships(age,gender):

	first_age = age[0]
	all_relations = []
	all_relations.append("Self")

	# flags
	wifeExist = False
	motherExist = False
	fatherExist = False
	gfatherExist = False
	gmotherExist = False

	try:
		# Iterate over all family members and define relations with head of family
		for i in range(1,len(age)):
			flag = 0
			curr_age = age[i]

			# If the age is -10 or +10 of first family member and gender male then consider relation as "Brother"
			if (curr_age >= (first_age - 10)) and (curr_age <= (first_age + 10)) and gender[i] == "M":
				all_relations.append("Brother")
				flag = 1
				continue

			# If the age is -10 or +10 of first family member and gender female then relation can be either "Wife" or "Sister"
			elif (curr_age >= (first_age - 10)) and (curr_age <= (first_age + 10)) and gender[i] == "F":

				# If wife is not considered then first consider wife over sister relation
				if wifeExist and (curr_age >= (first_age - 10)) and (curr_age <= (first_age + 10)):
					all_relations.append("Sister")
					flag = 1
					continue

				else:
					wifeExist = True
					all_relations.append("Wife")
					flag = 1
					continue

			# If age is greater than first member age 
			elif curr_age > first_age:

				# If age is in between +20 or +40 of first age then it can be mother or father based on genders
				if ((first_age <= curr_age - 20) and (first_age > curr_age - 40)):
					if not motherExist and gender[i] == "F":
						all_relations.append("Mother")
						flag = 1
						motherExist = True
						continue
					elif not fatherExist:
						all_relations.append("Father")
						flag = 1
						fatherExist = True
						continue

				# If age is in between +40 or +60 of first age then it can be grandmother or grandfather based on genders
				if ((first_age <= curr_age - 40) and (first_age > curr_age - 60)):
					if not gmotherExist and gender[i] == "F":
						all_relations.append("Grand-mother")
						flag = 1
						gmotherExist = True
						continue
					elif not gfatherExist:
						all_relations.append("Grand-father")
						flag = 1
						gfatherExist = True
						continue

			# If age is smaller than first member age
			elif curr_age < first_age:

				# If age is in between -20 or -40 of first age then it can be daughter or son based on genders 
				if (first_age - 20) >= curr_age > (first_age - 40):
					if gender[i] == "F":
						all_relations.append("Daughter")
						flag = 1
						continue
					else:
						all_relations.append("Son")
						flag = 1
						continue

				# If age is in between -40 or -60 of first age then it can be granddaughter or grandson based on genders
				if (first_age - 40) >= curr_age > (first_age - 60):
					if gender[i] == "F":
						all_relations.append("Grand-daughter")
						flag = 1
						continue
					else:
						all_relations.append("Grand-son")
						flag = 1
						continue
			# If no any relation then consider it as "Other"
			if flag==0:
				all_relations.append("Other")
	
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	return all_relations
	
############################## GET OCCUPATION ############################## 
# Function to get the occupation of all family members based on their ages

def get_occupation(age_lst, all_occupation):

	all_occ = all_occupation + ifp.occ_age_specific
	occupation = []

	try:
		for age in age_lst:
			if age > 75:
				occ = numpy.random.choice(ifp.occ_other,1)[0]
			if age <= 22:
				occ = "Unknown-3379182"
			if age >= 40 and age <= 75:
				occ = numpy.random.choice(all_occ,1)[0]
			if age > 22 and age < 40:
				occ = random.choice(all_occupation)
			
			occupation.append(occ.strip())
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	return occupation

############################## GET MARITAL STATUS ############################## 
# Function to get the marital status of all family members
def get_marital_status(age_lst,relations):
	marital_status = []	
	try:
		for i in range(0,len(relations)):
			status = "Single"
			rel = relations[i]
			age = age_lst[i]

			if rel == "Self":
				check_lst = ["Wife","Son","Daughter",'Grand-son',"Grand-daughter"]
				if any(x in check_lst for x in relations):
					status = "Married"
			elif (rel == "Brother" and age > 35) or (rel == "Sister" and age > 30):
				status = "Married"
			elif rel == "Wife" or rel == "Mother" or rel == "Father" or rel == "Grand-mother" or rel == "Grand-father":
				status = "Married"
			elif (rel == "Son" and age > 35) or (rel == "Daughter" and age > 30):
				status = "Married"
			elif (rel == "Grand-son" and age > 35) or (rel == "Grand-daughter" and age > 30):
				status = "Married"
			elif (rel == "Other" and age > 40):
				status = "Married"

			marital_status.append(status)
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	return marital_status
	
		
############################## GET MAIL ID'S ############################## 
# Function to get the mail id's

def get_email_id(family_member_name,family_last_name):
	random_domain = random.choice(ofp.domains)
	
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

############################## GET CELL AND WORK NUMBERS ############################## 
# Function to get the cell and work numbers using some fixed format

def get_phone_numbers():

	family_member_cell_check = numpy.random.choice(["y","n"], p=[0.7,0.3])

	family_member_work_check = numpy.random.choice(["y","n"],p=[0.5,0.5])

	try:
		if family_member_cell_check == "y":
			family_member_cell_number = "+1-"+str(random.randrange(100,999))+"-"+str(random.randrange(100,999))+"-"+str(random.randrange(1000,9999))
		else:
			family_member_cell_number = None

		if family_member_work_check == "y":
			family_member_work_number = "+1-"+str(random.randrange(100,999))+"-"+str(random.randrange(100,999))+"-"+str(random.randrange(1000,9999))
		else:
			family_member_work_number = None
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	return [family_member_cell_number, family_member_work_number]


############################## GET MIDDLE NAMES ############################## 
# Function to get the middle names for all family members

def get_middle_name(first_names_lst, all_relations, age, male_names_data):
	middle_names_lst = []
	grand_father_check = 0

	try:
		# Get middle names for all family members
		for i in range(0,len(all_relations)):
			middle_name = None

			# If person is self and "father" is present in all relations then get father's first name else generate randomly
			if all_relations[i] == "Self":
				if "Father" in all_relations:
					# get fathers first name
					father_index = all_relations.index("Father")
					middle_name = first_names_lst[father_index]
				else:
					middle_name = random.choice(male_names_data)
					random_father_name = middle_name

			# If relation is mother or brother or sister then get father's first name else take already generated name
			elif all_relations[i] == "Mother" or all_relations[i] == "Brother" or all_relations[i] == "Sister":
				if "Father" in all_relations:
					# get fathers first name
					father_index = all_relations.index("Father")
					middle_name = first_names_lst[father_index]
				else:
					middle_name = random_father_name

			# If relation is wife or daughter or son then take first name of self as middle name
			elif all_relations[i] == "Wife" or all_relations[i] == "Daughter" or all_relations[i] == "Son":
				self_index = all_relations.index("Self")
				middle_name = first_names_lst[self_index]
			
			# If relation is father of grandmother then if grandfather present then take first name of him else generate random name
			elif all_relations[i] == "Father" or all_relations[i] == "Grand-mother":
				if "Grand-father" in all_relations:
					# get grand-fathers first name
					grand_father_index = all_relations.index("Grand-father")
					middle_name = first_names_lst[grand_father_index]
				else:
					if grand_father_check == 0:
						grand_father_check = 1
						middle_name = random.choice(male_names_data)
						random_gfather_name = middle_name
					else:
						middle_name = random_gfather_name

			# If relation is grandfather then generate niddle name randomly
			elif all_relations[i] == "Grand-father":
				middle_name = random.choice(male_names_data)

			# If relation is grandson or granddaughter then if son present get his first name else generate randomly
			elif all_relations[i] == "Grand-son" or all_relations[i] == "Grand-daughter":
				if "Son" in all_relations:
					son_index = all_relations.index("Son")
					middle_name = first_names_lst[son_index]
				else:
					middle_name = random.choice(male_names_data)
				
			if middle_name is not None:
				middle_names_lst.append(middle_name.strip())
			else:
				middle_names_lst.append(middle_name)
				
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()


	return middle_names_lst

############################## GET ADDRESS ############################## 
# Function to get the mailing and residential address for each family

def get_address():
	# Generate fake address using faker package
	address = fake.address().split('\n')
	line1 = address[0]
	line2 = None
	
	try:
		if "," in address[0]:
				line = address[0].split(',')
				line1, line2 = line[0], line[1]
		elif 'apt' in address[0].lower() or "suite" in address[0].lower() or 'box' in address[0].lower():
				if 'apt' in address[0].lower():
					index = address[0].index("Apt")
				elif "suite" in address[0].lower():
					index = address[0].index("Suite")
				elif 'box' in address[0].lower():
					index = address[0].index("Box")
	  
				line1 = address[0][0:index]
				line2 = address[0][index:]

		if ',' in address[1]:
				combined_address = address[1].split(',')
				city = combined_address[0]
				state = combined_address[1].split()[0]
				zip_code = combined_address[1].split()[1]
		else:
				combined_address = address[1].split()
				city, state, zip_code = combined_address[0], combined_address[1], combined_address[2]

		if line2 is not None:
			line2 = line2.strip()
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	return [line1.strip(),line2,city,state,zip_code,"US"]
	


############################## GET VIN ##############################
global i
i = 0
def get_vin_data(age_lst, vin_license_data):
	vin = []
	license = []
	global i

	try:
		for age in age_lst:
			# If age in between 18 and 85 then assign vehicle to that member	
			if 18 < age <= 85:
				vin.append(vin_license_data["vin"][i])
				license.append(vin_license_data["license_plate_no"][i])
				i = i + 1
				
			else:
				vin.append(None)
				license.append(None)
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

		
	return [vin, license]
	

############################## GET ADDRESS ID ##############################

global data
data = {}
global id_data_lst
global address_index
address_index = -1

id_data = csv.reader(open(ifp.input_id_file))
id_data.next()
id_data_lst = list(id_data)

def get_address_id(family_member_cnt,age):
	global address_index
	age_cri = []
	address_id_lst = []
	
	try:
		for a in age:
			if 18 < a <= 85: 
				age_cri.append(a)

		# For all family members assign address id based on each policy to max 2 vehicles
		for j in range(family_member_cnt):
			if 18 < age[j] <= 85:
				address_id_lst.append(id_data_lst[address_index][4])
					
				if len(address_id_lst) < len(age_cri) and (len(address_id_lst)==2 or len(address_id_lst)==4):
					address_index = address_index + 1
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	return address_id_lst
			
############################## **************MAIN************ ##############################

def main():

	logging.info("In main function")
	final_data = []
	times = time.time()
	print "***********Getting data*************"
	try:
		engine = create_engine(dc.connection_string)
		connection = engine.connect()
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	try:
		# Get data from vehicles table to get vin numbers
		logging.info("Reading vehicles table to get vin numbers from it")
		metadata = MetaData(bind=None)
		table = Table(ifp.vehicle_table_name, metadata, autoload = True, autoload_with = engine)
		stmt = select([table])
		headers = metadata.tables[ifp.vehicle_table_name].columns.keys()

		vehicle_data = connection.execute(stmt).fetchall()
		vehicle_data = pd.DataFrame(vehicle_data,columns = headers)

		pool = Pool(processes=2)
		data_output_file = csv.writer(open(ofp.output_data_file,"w"))
		data_output_file.writerow(ofp.output_file_headers)

		logging.info("Reading felame and male first names text files")
		# read males and females first name files
		female_names_input_file = open(ifp.female_names_file,"r")
		female_names_data = female_names_input_file.readlines()

		male_names_input_file = open(ifp.male_names_file,"r")
		male_names_data = male_names_input_file.readlines()

		# read age probabily relation file to generate members according to that
		age_probability_data = list(csv.DictReader(open(ifp.age_probability_relation_file)))

		# read occupations file 
		all_occupation = open(ifp.occ_file,"r").readlines()

		# read unique id's data
		logging.info("Reading unique ID csv file")
		id_data = csv.reader(open(ifp.input_id_file))
		id_data.next()
		id_data_lst = list(id_data)
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()


	family_id = 0
	family_data_lst = []
	global address_index

	try:
		# Iterate over no of families mentioned in the config file
		logging.info("Creating data for families")
		for i in range(0,ofp.no_of_families):

			# Get addresses
			result = pool.apply_async(get_address, ())
			family_mailing_address = result.get()

			result1 = pool.apply_async(get_address, ())
			family_address = result1.get()


			family_id = family_id + 1

			# get family last name
			family_last_name = fake.last_name()
			family_home_number = "+1-"+str(random.randrange(100,999))+"-"+str(random.randrange(100,999))+"-"+str(random.randrange(1000,9999))
			family_member_cnt = random.randint(ofp.min_family_members,ofp.max_family_members)

			# generate genders for family members such that neither of the genders will be more in count
			while 1:
				gender = numpy.random.choice(["M","F"],family_member_cnt,p=[0.5,0.5])
				gender = list(gender)
				gender.sort(reverse=True)
				if family_member_cnt == 1:
					break

				if family_member_cnt > 1:
					cnt = family_member_cnt / 2
					if list(gender).count("M") >= cnt and list(gender).count("F") >= cnt:
						break

			# It will be list of dict containing family members of current family
			family_data = []

			DOB,age = get_dob(family_member_cnt, age_probability_data)

			all_relations = get_relationships(age,gender)
			
			occupation = get_occupation(age, all_occupation)
			
			marital_status = get_marital_status(age,all_relations)

			first_names_lst,gender_lst = get_first_name(gender,female_names_data, male_names_data)

			middle_names_lst = get_middle_name(first_names_lst,all_relations,age, male_names_data)

			vin, license = get_vin_data(age, vehicle_data)

			age_cri = []
			for a in age:
				if 18 < a <= 85: 
					age_cri.append(a)


			if (family_member_cnt == 1 and 18 < age[0] <= 85) or i==0: 
				address_index = address_index + 1
			elif family_member_cnt > 1 and len(age_cri) > 0:
				address_index = address_index + 1

			address_id_lst = get_address_id(family_member_cnt,age)
			
			k=0
			for _ in range(family_member_cnt):
				
				family_member_data = []
				
				if 18 < age[_] <= 85:
					address_id = address_id_lst[k]
					k=k+1
				else:
					address_id = None

				# Get Email
				family_member_email = get_email_id(first_names_lst[_],family_last_name)

				# Get phone numbers
				family_member_contact_numbers = get_phone_numbers()

				# Add all data in member list
				family_member_data.extend([family_id,address_id, first_names_lst[_], middle_names_lst[_], family_last_name, family_member_email])

				family_member_data.extend(family_mailing_address)

				family_member_data.extend(family_address)

				family_member_data.append(family_home_number)
				family_member_data.extend(family_member_contact_numbers)

				family_member_data.extend([gender_lst[_], DOB[_], license[_]])
							
				if all_relations[_]=="Self":
					family_member_data.extend([1,all_relations[_]])
				else:
					family_member_data.extend([0,all_relations[_]])

				family_member_data.extend([occupation[_], marital_status[_]])

							
				data_output_file.writerow(family_member_data)
				final_data.append(family_member_data)
		logging.info("Succesfully generated families data")
				
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()

	try:
		df = pd.DataFrame(final_data, columns=ofp.output_file_headers)
		df["dob"] =  pd.to_datetime(df["dob"])
		#df["dob"] = df["dob"].dt.round('1s')
		df.to_sql(ofp.table_name, engine, index=False)
		logging.info("Successfully loaded " + str(ofp.no_of_families) + " families data into database")
	except Exception,e:
		print str(e)
		logging.info(traceback.format_exc())
		exit()
	
	timee = time.time()
	print(timee-times)

		
if __name__=="__main__":
	main()