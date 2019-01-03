import csv
import sys

#Importing configuration file
sys.path.insert(0, "../Config")
import Config_DataSplitter as conf

def split():
	line_count = 0
	othercars = []
	expcars = []

	#Input file consisting of all cars
	with open(conf.input_file_path) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			if line_count == 0:
			#Copy the headers as it is to both the files
				line_count += 1
				with open(conf.othercar_file_path, 'w') as writeFile1:
					writer1 = csv.writer(writeFile1)
					writer1.writerow(row)
					writeFile1.close()
				with open(conf.expcar_file_path, 'w') as writeFile2:
					writer2 = csv.writer(writeFile2)
					writer2.writerow(row)
					writeFile2.close()
			else:
			#Check if current car is a expensive(rare) 
				carname = [ x for x in conf.expensive_cars if row[1] == x]
				if carname == []:
					othercars.append(row)
				else:
					expcars.append(row)
			line_count += 1

	print(str(line_count)+" records processed!")

	writer1 = csv.writer(open(conf.othercar_file_path, 'a'))
	writer1.writerows(othercars)

	writer2 = csv.writer(open(conf.expcar_file_path, 'a'))
	writer2.writerows(expcars)

	writeFile1.close()
	writeFile2.close()

def main():
	split()
	
if __name__ == "__main__":
	main()
