import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Specify the instance ID
instance_id = 'i-04f45f3e7a143fc69'  # Replace with your EC2 instance ID

try:
    # Stop the instance
    response = ec2.stop_instances(InstanceIds=[instance_id])
    # Retrieve the current state of the instance
    current_state = response['StoppingInstances'][0]['CurrentState']['Name']
    print(f"Instance '{instance_id}' is in the process of being stopped. Current state: {current_state}.")
except Exception as e:
    print(f"Error stopping instance: {e}")
