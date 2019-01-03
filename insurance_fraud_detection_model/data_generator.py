import faker
import csv
import random

f=faker.Faker("en_US")
print(f.email())

input_file = csv.DictReader(open("Address file.csv"))

output_file = csv.writer(open('data.csv', 'w'))

header = ["Name","Address","Phone Number","DOB","Licence Number"]
#final_data.append(header)
output_file.writerow(header)

cnt = 0
for row in input_file:
    if row['ca_street_number']!="NULL" and row['ca_street_name']!="NULL" and row['ca_street_type']!="NULL" and row['ca_city']!="NULL":
        cnt = cnt + 1
        name = f.name()
        print(name)
        address = row['ca_street_number'] + "," + row['ca_street_name'] + row['ca_street_type'] + "," + row['ca_city'] + "," + "US"
        #print(address)
        repeat_no = random.randint(1,5)
        print(repeat_no)
        for _ in range(repeat_no):
            member_name = f.name()
            member_full_name = member_name.split()[0] + " " + name.split()[1]
	    number = "+1-"+str(random.randrange(100,999))+"-"+str(random.randrange(100,999))+"-"+str(random.randrange(1000,9999))
	    
            output_file.writerow([member_full_name,address, number, f.date_of_birth(), f.license_plate()])
            

    if cnt == 100:
        break
        
   

'''with open('data.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(final_data)'''
