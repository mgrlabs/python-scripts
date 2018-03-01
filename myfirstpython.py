#!/usr/bin/python
import boto3


# # Let's use Amazon S3
# s3 = boto3.resource('s3')

# ec2 = boto3.resource('ec2')
# instance = ec2.Instance('i-0c5b4a39d38e5a626')

# #for bucket in s3.buckets.all():
# #    print(bucket.name)

# for instance in ec2.instances.all():
#     print(instance.instance_id, instance.state)


# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# List metrics through the pagination interface
paginator = cloudwatch.get_paginator('list_metrics')
for response in paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],
                                   MetricName='IncomingLogEvents',
                                   Namespace='AWS/Logs'):
    print(response['Metrics'])