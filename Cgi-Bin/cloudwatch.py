#!/usr/bin/env python3

import boto3
import json
from datetime import datetime, timedelta
import cgi
import cgitb

cgitb.enable()

print("Content-Type: application/json")
print()

# Get the form data
form = cgi.FieldStorage()

aws_access_key_id = form.getfirst('aws_access_key_id', '').strip()
aws_secret_access_key = form.getfirst('aws_secret_access_key', '').strip()
region_name = form.getfirst('region_name', '').strip()
namespace = form.getfirst('namespace', '').strip()
metric_name = form.getfirst('metric_name', '').strip()
instance_id = form.getfirst('instance_id', '').strip()

# Create a CloudWatch client
try:
    cloudwatch = boto3.client(
        'cloudwatch',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
except Exception as e:
    print(json.dumps({"error": str(e)}))
    exit()

# Define the time range for the metrics
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=1)

# Call the get_metric_statistics method
try:
    response = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,  # Period in seconds (e.g., 300 seconds = 5 minutes)
        Statistics=['Average'],  # Type of statistics (e.g., Average, Sum, Maximum, Minimum, SampleCount)
        Unit='Percent'  # Unit of the metric
    )

    # Extract the retrieved data points and prepare JSON response
    data_points = [{'Time': dp['Timestamp'].isoformat(), 'Average': dp['Average']} for dp in response['Datapoints']]
    print(json.dumps(data_points))

except Exception as e:
    print(json.dumps({"error": str(e)}))
