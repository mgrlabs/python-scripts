#!/usr/bin/python

import boto3
import csv
import panda as pd
import numpy as np

# with open('ALH_CloudWatch.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print row

# with open('ALH_CloudWatch.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         if row[0] == 'humanReadableTimestamp':
#             print(row[0])        


# sourceCSV = open('ALH_CloudWatch.csv', 'r')
# readerCSV = csv.reader(sourceCSV, delimiter=',')

# for row in readerCSV:
#     print(row[4])

df = pd.read_csv('ALH_CloudWatch.csv')
df