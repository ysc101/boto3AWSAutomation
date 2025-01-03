import boto3

s3 = boto3.resource('s3')

# File path, bucket name, and key
file_path = r"C:\Users\Yogesh.c\Desktop\My_Data\s3save\yogesh.txt"
bucket_name = "bucketofyogesh"
key_name = "yogesh.txt"

# Upload file to S3
s3.meta.client.upload_file(Filename=file_path, Bucket=bucket_name, Key=key_name)
print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{key_name}'Successfully.")
