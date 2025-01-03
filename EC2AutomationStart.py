import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Specify instance ID
instance_id = 'i-04f45f3e7a143fc69'

try:
    # Start the instance
    response = ec2.start_instances(InstanceIds=[instance_id])
    print(f"Instance '{instance_id}' is starting...")
except Exception as e:
    print(f"Error starting instance: {e}")