import boto3

aws_access_key_id = "##############"
aws_secret_access_key = "##############"
aws_session_token = "##############"

client = boto3.client('rekognition', aws_session_token=aws_session_token, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name="us-east-1")

response = client.create_collection(
    CollectionId = "GeneseCollection"
)

print(response)