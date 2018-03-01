#!/usr/bin/python
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-0c5b4a39d38e5a626')

#for bucket in s3.buckets.all():
#    print(bucket.name)

print(instance.name)
