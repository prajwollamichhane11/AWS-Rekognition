import boto3
import base64
import json


aws_access_key_id = "##############"
aws_secret_access_key = "##############"
aws_session_token = "##############"

# Calling the clients rekognition among several clients
client = boto3.client('rekognition', aws_session_token=aws_session_token, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name="us-east-1")
# client = boto3.client('rekognition', aws_session_token=os.getenv('aws_session_token'), aws_access_key_id=os.getenv('aws_access_key_id'), aws_secret_access_key=os.getenv('aws_secret_access_key'), region_name="us-east-1")

file = open('prajwol.jpg','rb').read()

response = client.detect_faces(
    Image = {
        'Bytes':file
    },
    Attributes=['ALL']
)

# print(response['FaceDetails'])

for face in response['FaceDetails']:
    print(json.dumps(face, indent=4, sort_keys=True))