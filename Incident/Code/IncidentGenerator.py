import csv
import time
import sys
import numpy
import random
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

#Import file truncate
import truncate_table as tt

#Importing configuration file
sys.path.insert(0, "../Config")
import Config_incident as Iconf

i=1
id = '0'
VIN_list = []
incident_list = []
relations = ["Self", "Spouse", "Brother", "Sister", "Mother", "Father", "Son", "Daughter", "Third Party"]

#Connect to postgres
engine = create_engine('postgresql://data:gen123@10.20.202.43:5432/datagen')
db_connection = engine.connect()

#Load coverage table
select = text("SELECT * FROM coverage")
result = db_connection.execute(select)
VIN_list = pd.DataFrame(list(result), columns = result.keys())['vin'].unique().tolist()
num_rec = random.randint(len(VIN_list)-20000, len(VIN_list))

#Load incident descriptions
reader = csv.reader(open(Iconf.inc_des_path))
incident_desc_list = list(reader)

start = time.time()

while(i <= num_rec):
    val=5-len(str(i))
    inc_incident_id = "INC01-1"+id*val+str(i)
    value = random.randint(0,len(VIN_list))

    if value == len(VIN_list):
	value = value - 1

    inc_vehicle_id = VIN_list[value] 
    VIN_list.pop(value)

    incident_desc = random.choice(incident_desc_list)

    driver = random.choice(relations)

    inc_is_the_vehicle_driveable = numpy.random.choice(["Y",""],p = [0.8,0.2])

    incident_list.append([inc_incident_id, inc_vehicle_id, incident_desc[0], driver, inc_is_the_vehicle_driveable])

    i = i + 1


print("Generate: "+str(time.time()-start))

#Truncate table if exists
if engine.dialect.has_table(engine, Iconf.table_name):
	tt.truncate(Iconf.table_name)

#Create table with the specified columns
df = pd.DataFrame.from_records(incident_list, columns=Iconf.headers)

#Load to database
df.to_sql(Iconf.table_name, engine, index=False)

print(str(i)+" Records Generated and loaded to DB!")