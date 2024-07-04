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
    aws_access_key_id='AKIA6ODU5BZPJXUEGHOD',
    aws_secret_access_key='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'
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
# Handle CGI form input
#form = cgi.FieldStorage()
#action = form.getvalue('action')
#instance_id = form.getvalue('instance_id')

#print("Content-type: text/html\n")

#if action == "launch":
 #   instance_id = osiLaunch()
  #  print(f"Instance launched: {instance_id}")
#elif action == "terminate" and instance_id:
 #   response = terminate_instance(instance_id)
  #  print(f"Terminated instance {instance_id}: {response}")
#else:
 #   print("Invalid action or missing instance ID.")
