import boto3

# Initialize IAM client
iam = boto3.client('iam')

# Specify user name
user_name = 'testuser'

try:
    # Create a new IAM user
    response = iam.create_user(UserName=user_name)
    print(f"User '{user_name}' created successfully.")
except Exception as e:
    print(f"Error creating user: {e}")
