#!/usr/bin/python3
import cgi
import boto3
import os
print("Content-type:text/html")
print("")
# Configure the boto3 resource
myec2 = boto3.resource(
    'ec2',
    region_name='ap-south-1',
    aws_access_key_id='',
    aws_secret_access_key=''
)

def osiLaunch():

    instances = myec2.create_instances(
        InstanceType='t2.micro',
        ImageId='ami-022ce6f32988af5fa',
        MaxCount=1,
        MinCount=1
    )
    return instances



def terminate_instance(instance_id):
    try:
        instance = myec2.Instance(instance_id)
        response = instance.terminate()
        return response
    except Exception as e:
        return str(e)
result = osiLaunch()
print(result)
