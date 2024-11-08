# EC2 Start/Stop Lambda Script

This project contains a Lambda function script that starts and stops all EC2 instances in an AWS account based on a specified action. Additionally, it demonstrates how to set up a cron job to automate these actions on a schedule.

## Prerequisites

- **AWS Account**: You’ll need an active AWS account with permissions to access EC2 and Lambda services.
- **Python Environment**: The Lambda function is written in Python.

## Project Overview

### What is EC2?

Amazon EC2 (Elastic Compute Cloud) is a web service provided by AWS to create virtual servers, known as instances, in the cloud. With EC2, you can run applications on virtual machines without needing to manage physical servers.

### What is AWS Lambda?

AWS Lambda is a compute service that lets you run code in response to events without managing servers. In this project, Lambda will handle starting and stopping EC2 instances when triggered.

### Lambda Role Requirements

To allow Lambda to interact with EC2, you’ll need to create an AWS IAM role with appropriate permissions:

1. **Create an IAM Role** with the following permissions:
    - `ec2:DescribeInstances`
    - `ec2:StartInstances`
    - `ec2:StopInstances`
2. Attach this role to your Lambda function.

## Script Details

### Code Explanation

The provided Lambda function uses **boto3**, AWS's SDK for Python, to connect to EC2 and perform actions based on an event trigger.

```python
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    action = event['action']
    instances = ec2.describe_instances()
    instance_ids = [instance['InstanceId'] for reservation in instances['Reservations'] for instance in reservation['Instances']]
    
    if action == 'start':
        if instance_ids:
            ec2.start_instances(InstanceIds=instance_ids)
            print("Starting instances:", instance_ids)
        else:
            print("No instances found to start")
    
    elif action == 'stop':
        if instance_ids:
            ec2.stop_instances(InstanceIds=instance_ids)
            print("Stopping instances:", instance_ids)
        else:
            print("No instances found to stop")
    
    else:
        print("Invalid action provided in the event")


