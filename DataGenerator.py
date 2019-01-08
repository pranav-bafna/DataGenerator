import csv
import random
import numpy
import sys
import time

#Importing file splitter 
import DataSplitter as ds

#Importing configuration file
sys.path.insert(0, "../Config")
import Config_DataGenerator as DGconf

def Generate():
	i = 0
	vin_data = []
	data_list = []

	reader_expcars = csv.reader(open(DGconf.expcar_file_path))
	expcar_data = list(reader_expcars)
	
	reader_othercars = csv.reader(open(DGconf.othercar_file_path))
	othercar_data = list(reader_othercars)
	data_size = len(othercar_data)
	
	reader2 = csv.reader(open(DGconf.VIN_file_path))
	vin_data = list(reader2)

	with open(DGconf.vehicle_data_path, 'w') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerow(DGconf.headers)
		writeFile.close()
	
	start = time.time()
	
	while (i < DGconf.num_records):
		#Make a probability based random choice for car
		file_data = numpy.random.choice([expcar_data, othercar_data], p = DGconf.car_distribution)
		#Choose random car from the list
		chosen_car = random.choice(file_data)
		#Choose unique VIN
		chosen_row = vin_data[i+1]
		#Car price is generated based on type of car
		if len(file_data) == data_size:
			price = random.randint(DGconf.min_othercar_price, DGconf.max_othercar_price)
		else:
			price = random.randint(DGconf.min_expcar_price, DGconf.max_expcar_price)
		#Randomly generated car age
		car_age = random.randint(DGconf.min_car_age, DGconf.max_car_age)
		#Randomly generated car mileage
		car_mileage = random.randint(DGconf.min_car_mileage, DGconf.max_car_mileage)
		data_list.append([chosen_row[0], chosen_row[1], chosen_car[1], chosen_car[2], chosen_car[0], price, car_age, car_mileage])
		i = i+1

	gen = time.time()
	print("Generation: "+str(gen-start))
	print(str(i)+" Records processed!")
	
	with open(DGconf.vehicle_data_path, 'a') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(data_list)
		writeFile.close()
	print("Write: "+str(time.time()-gen))
	print(str(len(data_list))+" Records written!")

def main():
	ds.split()
	Generate()
	
if __name__ == "__main__":
	main()
