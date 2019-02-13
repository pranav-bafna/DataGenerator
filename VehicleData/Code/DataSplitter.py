import os
import time
import logging

if not os.path.exists(r'../logs'):
	os.makedirs(r'../logs')

timestamp = time.strftime("%d-%m-%Y_%I-%M-%S")
log_file = "../logs/vehicle_data_splitter_" + timestamp + ".log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.debug("Vehicle data splitting is started.")

try:
	import csv
	import sys

	#Importing configuration file
	sys.path.insert(0, "../Config")
	import Config_DataSplitter as conf

except Exception,e:
	print(str(e))
	logging.debug(traceback.format_exc())
	exit()


def split():
	othercars = []
	expcars = []

	try:
		#Load file consisting of all cars
		car_reader = csv.reader(open(conf.input_file_path))
		car_list = list(car_reader)

		#Create other car file and write headers
		with open(conf.othercar_file_path, 'w') as writeFile1:
			writer1 = csv.writer(writeFile1)
			writer1.writerow(car_list[0])
			writeFile1.close()

		#Create expensive car file and write headers
		with open(conf.expcar_file_path, 'w') as writeFile:
			writer = csv.writer(writeFile)
			writer.writerow(car_list[0])
			writeFile.close()

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	i = 1

	try:
		while(i < len(car_list)):
			#Check if current car is a expensive(rare) 
			carname = [ x for x in conf.expensive_cars if car_list[i][1] == x]
	
			if carname == []:
				othercars.append(car_list[i])
	
			else:
				expcars.append(car_list[i])

			i = i + 1
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	print(str(len(car_list))+" records processed!")
	logging.debug(str(len(car_list))+" records processed!")

	try:
		writer1 = csv.writer(open(conf.othercar_file_path, 'a'))
		writer1.writerows(othercars)
		logging.debug(str(len(othercars))+" records written to "+conf.othercar_file_path)
	
	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

	try:
		writer2 = csv.writer(open(conf.expcar_file_path, 'a'))
		writer2.writerows(expcars)
		logging.debug(str(len(expcars))+" records written to "+conf.expcar_file_path)

	except Exception,e:
		print(str(e))
		logging.debug(traceback.format_exc())
		exit()

def main():
	split()
	
if __name__ == "__main__":
	main()
