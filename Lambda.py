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
