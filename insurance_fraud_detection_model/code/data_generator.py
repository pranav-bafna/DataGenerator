# Import all required modules

# Import faker to generate fake data
import faker
import csv
import random
import time   
import threading   
from multiprocessing import Pool                                                                                                                                                                                            

# Import sys to be able to import config python files
import sys
sys.path.insert(0, '../configuration')

# Input path file present in "configuration folder"
import input_file_paths as ifp

# Import Output path file present in "configuration folder"
import output_file_paths as ofp

import numpy
from datetime import datetime, date

from string import ascii_uppercase,digits
import uuid

fake = faker.Faker("en_US")

# function to get first name and genders of all family members
def get_first_name(gender, female_names_data, male_names_data):

	first_names_lst = []
	gender_lst = []

	for gen in gender:	
		if gen == "F":
			first_names_lst.append(random.choice(female_names_data).strip())
			gender_lst.append("Female")
		else:
                	first_names_lst.append(random.choice(male_names_data).strip())
                	gender_lst.append("Male")

	return [first_names_lst,gender_lst]

# function to get date of births and age of all family members
def get_dob(family_member_cnt, age_probability_data):

	dgy = ofp.data_genearation_year
	i = 0
	DOB = []
	while(1):
		year_lst = []
		prob_lst = []
		for row in age_probability_data:
			year = (random.randint((dgy - int(row["max_age"])),(dgy - int(row["min_age"]))))
			year_lst.append(year)
			prob_lst.append(row["probability"])

		num = numpy.random.choice(year_lst,family_member_cnt, replace=False, p=prob_lst)
		if int(num[0]) < (dgy - 25):
			break

	while(i < family_member_cnt):
    		month = random.choice(range(1,13))
    		if month == 2:
        		day = random.choice(range(1, 29))
    		else:
        		day = random.choice(range(1, 31))
    		birth_date = datetime(num[i], month, day).isoformat().strip().split("T")[0]
    		DOB.append(birth_date)
    		i = i+1

	age = []
	for member in DOB: 
		age.append(int(str((datetime(dgy,1,1).date() - datetime.strptime(str(member).split()[0], '%Y-%m-%d').date())/365).split()[0]))

	return [DOB,age]
   
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

	for i in range(1,len(age)):
		flag = 0
		curr_age = age[i]
		if (curr_age >= (first_age - 10)) and (curr_age <= (first_age + 10)) and gender[i] == "M":
			all_relations.append("Brother")
			flag = 1
			continue

    		elif (curr_age >= (first_age - 10)) and (curr_age <= (first_age + 10)) and gender[i] == "F":
        		if wifeExist and (curr_age >= (first_age - 10)) and (curr_age <= (first_age + 10)):
				all_relations.append("Sister")
				flag = 1
				continue

                    	else:
				wifeExist = True
				all_relations.append("Wife")
				flag = 1
				continue

		elif curr_age > first_age:
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

		elif curr_age < first_age:
			if (first_age - 20) >= curr_age > (first_age - 40):
				if gender[i] == "F":
					all_relations.append("Daughter")
					flag = 1
					continue
				else:
					all_relations.append("Son")
					flag = 1
					continue

			if (first_age - 40) >= curr_age > (first_age - 60):
				if gender[i] == "F":
					all_relations.append("Grand-daughter")
					flag = 1
					continue
				else:
					all_relations.append("Grand-son")
					flag = 1
					continue
		if flag==0:
			all_relations.append("Other")


	return all_relations
	
# Function to get the occupation of all family members based on their ages
def get_occupation(age_lst, all_occupation):

	all_occ = all_occupation + ifp.occ_age_specific
	occupation = []

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

	return occupation


# Function to get the marital status of all family members
def get_marital_status(age_lst,relations):
	marital_status = []	
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

	return marital_status
			
	
# Function to get the mail id's
def get_email_id(family_member_name,family_last_name):
	random_domain = random.choice(ofp.domains)
	
	email_format = numpy.random.choice([1,2,3],p=[0.34,0.34,0.32])
	if email_format == 1:
		family_member_email = family_member_name.lower() + "." + family_last_name.lower() + "@" +random_domain + ".com"
	elif email_format == 2:
		family_member_email = family_member_name.lower()[0] + family_last_name.lower() + str(random.randrange(100,999)) + "@" +random_domain + ".com"
	elif email_format == 3:
		family_member_email = family_last_name.lower() + family_member_name.lower()[0] + str(random.randrange(10,999)) + "@" +random_domain + ".com"
	
	return family_member_email

# Function to get the cell and work numbers
def get_phone_numbers():

	family_member_cell_check = numpy.random.choice(["y","n"], p=[0.7,0.3])

	family_member_work_check = numpy.random.choice(["y","n"],p=[0.5,0.5])

	if family_member_cell_check == "y":
		family_member_cell_number = "+1-"+str(random.randrange(100,999))+"-"+str(random.randrange(100,999))+"-"+str(random.randrange(1000,9999))
	else:
		family_member_cell_number = ""

	if family_member_work_check == "y":
		family_member_work_number = "+1-"+str(random.randrange(100,999))+"-"+str(random.randrange(100,999))+"-"+str(random.randrange(1000,9999))
	else:
		family_member_work_number = ""

	return [family_member_cell_number, family_member_work_number]

# Function to get the middle names for all family members
def get_middle_name(first_names_lst, all_relations, age, male_names_data):
	middle_names_lst = []
	grand_father_check = 0
	for i in range(0,len(all_relations)):
		middle_name = ""
		if all_relations[i] == "Self":
			if "Father" in all_relations:
				# get fathers first name
				father_index = all_relations.index("Father")
				middle_name = first_names_lst[father_index]
			else:
                		middle_name = random.choice(male_names_data)
				random_father_name = middle_name

		elif all_relations[i] == "Mother" or all_relations[i] == "Brother" or all_relations[i] == "Sister":
			if "Father" in all_relations:
				# get fathers first name
				father_index = all_relations.index("Father")
				middle_name = first_names_lst[father_index]
			else:
				middle_name = random_father_name

		elif all_relations[i] == "Wife" or all_relations[i] == "Daughter" or all_relations[i] == "Son":
			self_index = all_relations.index("Self")
			middle_name = first_names_lst[self_index]
		
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

		elif all_relations[i] == "Grand-father":
                	middle_name = random.choice(male_names_data)

		elif all_relations[i] == "Grand-son" or all_relations[i] == "Grand-daughter":
			if "Son" in all_relations:
				son_index = all_relations.index("Son")
				middle_name = first_names_lst[son_index]
			else:
                		middle_name = random.choice(male_names_data)
			
		middle_names_lst.append(middle_name.strip())

	return middle_names_lst

# Function to get the mailing and residential address for each family
def get_address():
	address = fake.address().split('\n')
	line1 = address[0]
	line2 = ""
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

	return [line1.strip(),line2.strip(),city,state,zip_code,"US"]
	#data["mailing_address"]=[line1.strip(),line2.strip(),city,state,zip_code,"US"]

	'''if type == "m":
		data["mailing_address"]=[line1.strip(),line2.strip(),city,state,zip_code,"US"]
	else:
		data["residential_address"]=[line1.strip(),line2.strip(),city,state,zip_code,"US"]'''

global i
i = 0
def get_vin_data(age_lst, vin_license_data):
	vin = []
	license = []
	random_data = "n"
	global i

	for age in age_lst:
		'''if 18 < age <= 22:
			random_data = numpy.random.choice(["y","n"],p=[0.1,0.9])

		elif 22 < age <= 70:
			random_data = numpy.random.choice(["y","n"],p=[1,0])
		
		elif age > 70:
			random_data = numpy.random.choice(["y","n"],p=[0.9,0.1])
		
		
		if random_data == "y":
			vin.append(vin_license_data[i][0])
			license.append(vin_license_data[i][1])
			i = i + 1
			
		else:
			vin.append("")
			license.append("")'''
		
		if 18 < age <= 85:
			vin.append(vin_license_data[i][0])
			license.append(vin_license_data[i][1])
			i = i + 1
			
		else:
			vin.append("")
			license.append("")

		
	return [vin, license]
	
def get_coverage_data(coverage_data):
	
	random_coverage = random.choice(coverage_data)

	return random_coverage

global data
data = {}

def main():
	times = time.time()
	print "***********Getting data*************"
	pool = Pool(processes=2)
	data_output_file = csv.writer(open(ofp.output_data_file,"w"))
	data_output_file.writerow(ofp.output_file_headers)

	female_names_input_file = open(ifp.female_names_file,"r")
	female_names_data = female_names_input_file.readlines()

	male_names_input_file = open(ifp.male_names_file,"r")
	male_names_data = male_names_input_file.readlines()

	age_probability_data = list(csv.DictReader(open(ifp.age_probability_relation_file)))

        all_occupation = open(ifp.occ_file,"r").readlines()

	coverage_input_file = csv.reader(open(ifp.coverage_limit_file))
	coverage_input_file.next()
	coverage_data = list(coverage_input_file)

	vin_data = csv.reader(open(ifp.vin_data_file))
	vin_data.next()
	vin_license_data = list(vin_data)

	family_id = 0
	family_data_lst = []
	# Iterate over addresses input file
	#for address in address_input_file:
	for i in range(0,ofp.no_of_families):
		time1 = time.time()
		#family_mailing_address = get_address()
		#t1 = threading.Thread(target=get_address, args=())
		result = pool.apply_async(get_address, ())
		family_mailing_address = result.get()

		time2 = time.time()
		#family_address = get_address()
		result1 = pool.apply_async(get_address, ())
		family_address = result1.get()


		#t2 = threading.Thread(target=get_address1, args=())
		

		'''t1.start()
		t2.start()

		t1.join()
		t2.join()

		family_mailing_address = data["mailing_address"]
		family_address = data["residential_address"]'''

		family_id = family_id + 1

		family_last_name = fake.last_name()
		family_home_number = "+1-"+str(random.randrange(100,999))+"-"+str(random.randrange(100,999))+"-"+str(random.randrange(1000,9999))
		family_member_cnt = random.randint(ofp.min_family_members,ofp.max_family_members)

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

		time3 = time.time()
		# It will be list of dict containing family members of current family
		family_data = []

		DOB,age = get_dob(family_member_cnt, age_probability_data)
		#print DOB,age,gender
		time4 = time.time()


		all_relations = get_relationships(age,gender)
		time5 = time.time()
		
		occupation = get_occupation(age, all_occupation)
		time6 = time.time()
		
		marital_status = get_marital_status(age,all_relations)
		time7 = time.time()

		first_names_lst,gender_lst = get_first_name(gender,female_names_data, male_names_data)
		time8= time.time()

		middle_names_lst = get_middle_name(first_names_lst,all_relations,age, male_names_data)
		time9= time.time()

		vin, license = get_vin_data(age, vin_license_data)
		time10 = time.time()

		coverage = get_coverage_data(coverage_data)
		time11 = time.time()

		for _ in range(family_member_cnt):
			
			family_member_data = []
			
			# Get Email
			family_member_email = get_email_id(first_names_lst[_],family_last_name)
			time12 = time.time()

			# Get Licence No
			#family_member_licence = fake.license_plate().encode('utf-8')

			# Get phone numbers
			family_member_contact_numbers = get_phone_numbers()
			time13 = time.time()

			# Add all data in member list
			family_member_data.extend([family_id, first_names_lst[_], middle_names_lst[_], family_last_name, family_member_email])

			family_member_data.extend(family_mailing_address)

			family_member_data.extend(family_address)

			family_member_data.append(family_home_number)
			family_member_data.extend(family_member_contact_numbers)

			family_member_data.extend([gender_lst[_], DOB[_], license[_], vin[_]])
						
			if license[_]!="":
				family_member_data.extend(coverage)
			else:
				family_member_data.extend(["","",""])

			family_member_data.append(age[_])

			if all_relations[_]=="Self":
				family_member_data.extend([1,""])
			else:
				family_member_data.extend([0,all_relations[_]])

			family_member_data.extend([occupation[_], marital_status[_]])

			'''temp_lst = []
			temp_lst.append(ofp.output_file_headers)
			temp_lst.append(family_member_data)

			family_member_dict = [dict(zip(temp_lst[0], c)) for c in temp_lst[1:]]
			
			# Add member data in family list
			family_data.append(family_member_dict[0])'''
			
			family_data_lst.append(family_member_data)
			time14 = time.time()

	data_output_file.writerows(family_data_lst)
	time15 = time.time()

	'''print(time1 - times)
	print(time2 - time1)
	print(time3 - time2)
	print(time4 - time3)
	print(time5 - time4)
	print(time6 - time5)
	print(time7 - time6)
	print(time8 - time7)
	print(time9 - time8)
	print(time10 - time9)
	print(time11 - time10)
	print(time12 - time11)
	print(time13 - time12)
	print(time14 - time13)
	print(time15 - time14)'''
	print(time15-times)

			

if __name__=="__main__":
	main()