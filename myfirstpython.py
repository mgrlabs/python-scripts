#!/usr/bin/python
import boto3
import csv

# with open('ALH_CloudWatch.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print row

with open('ALH_CloudWatch.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
    if row[0] == 'humanReadableTimestamp':
        print(row[0])        