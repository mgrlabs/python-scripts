#!/usr/bin/python
import boto3
import csv

with open('ALH_CloudWatch.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print row