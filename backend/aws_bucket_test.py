import boto3
import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

root = environ.Path(__file__) - 3
env = environ.Env(
     DEBUG=(bool, False)
)
env_file = os.path.join(BASE_DIR, ".env")

environ.Env.read_env(env_file)  

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id=env('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=env('AWS_SECRET_ACCESS_KEY')
)

for bucket in s3.buckets.all():
    print(bucket.name)