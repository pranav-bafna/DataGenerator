import csv
input_file_path = "../Input/Coverage_Limits.csv"
output_file_path = "../Output/coverage_limits.csv"
file_headers = ["Coverage_id", "Coverage_name", "Coverage_limit"]
with open(input_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    coverage_id = 0
    for row in csv_reader:
        if coverage_id == 0:
            coverage_id += 1
            with open(output_file_path, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow(file_headers)
                writeFile.close()
        else:
            with open(output_file_path, 'a') as writeFile:
                writer = csv.writer(writeFile)
		row[1] = row[1].replace("/", "-")
                line = [coverage_id,row[0],row[1]]
                writer.writerow(line)
		coverage_id += 1
writeFile.close()
csv_file.close()
print("Done! "+str(coverage_id - 1)+" records written!")