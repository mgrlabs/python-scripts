#!/usr/bin/python
import boto3
import csv

# with open('ALH_CloudWatch.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print row

# with open('ALH_CloudWatch.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         if row[0] == 'humanReadableTimestamp':
#             print(row[0])        


datafile = open('ALH_CloudWatch.csv', 'r')
myreader = csv.reader(datafile, delimiter=',')
rowcount = 0
uniqueId = 'start'

for row in myreader:
    if uniqueId == row[4]:
        rowcount = rowcount +1
    else:
        print(rowcount)
        rowcount = 0
        uniqueId = row[4]
    