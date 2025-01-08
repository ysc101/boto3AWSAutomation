import boto3

iam=boto3.client('IAM')

username="myuser"
try:
    response=iam.create_user(User_Name=username)
    print(f"User {username}creted successfully")
except Exception as e:
    print(f"    Error Creating User: {e}")

