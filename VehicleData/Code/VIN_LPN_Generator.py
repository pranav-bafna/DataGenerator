import numpy
import random
import time
import uuid
import csv
from collections import OrderedDict
numpy.random.seed(int(time.time()))

VIN_LPN_list=[]
num_records = 1000000
file_path = "Unique_VIN_Data1.csv"
headers = ["VIN", "License Plate No"]

x = list(str(i) for i in range(1,10000))
digits = [''.join(i) for i in x]
digits_unique = []
for d in range(len(digits)):
    L = 4-len(digits[d])
    digits[d] = L*'0'+digits[d]
    
    #Get only those numbers with nothing repeated
    if(digits[d] == ''.join(list(OrderedDict.fromkeys(digits[d])))):
        digits_unique.append(digits[d])
   
len(digits_unique)

x = list(chr(i) for i in range(65,91))
y = list(chr(i) for i in range(65,91))
#y = list(str(i) for i in range(1,100))
transpose1 = numpy.transpose([numpy.tile(x, len(y)), numpy.repeat(y, len(x))])
temp = [''.join(list(i)) for i in transpose1]
transpose2 = numpy.transpose([numpy.tile(x, len(temp)), numpy.repeat(temp, len(x))])
letters = [''.join(list(i))+' ' for i in transpose2]


letters_unique = []
#Get only those letter sequences with nothing repeated
for L in range(len(letters)):
    if(letters[L] == ''.join(list(OrderedDict.fromkeys(letters[L])))):
        letters_unique.append(letters[L])

len(letters_unique)

a = time.time()
plates = numpy.transpose([numpy.tile(letters_unique, len(digits_unique)), numpy.repeat(digits_unique, len(letters_unique))])
b = time.time()
print ('cartesian join took',b-a,'secs')
indices = numpy.random.choice(range(len(plates)),num_records, replace=False)
c = time.time()
print ('random indices took',c-b,'secs')
plates_5m = [''.join(i) for i in plates[indices]]
d = time.time()
print ('join took',d-c,'secs')

i=0
while(i<num_records):
    VIN = str(uuid.uuid4()).upper().replace("-","")[0:16]
    VIN_LPN_list.append([VIN,plates_5m[i]])
    i = i+1

writer = csv.writer(open(file_path, 'w'))
writer.writerow(headers)

with open(file_path, 'a') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(VIN_LPN_list)
    writeFile.close()