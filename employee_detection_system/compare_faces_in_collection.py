import boto3
import base64
import json

aws_access_key_id = "##############"
aws_secret_access_key = "##############"
aws_session_token = "##############"

client = boto3.client('rekognition', aws_session_token=aws_session_token, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name="us-east-1")

file = open('rajesh.jpg','rb').read()

CollectionId = "GeneseCollection"


response = client.detect_faces(
    Image = {
        "Bytes" : file
    }
)
# print(response['FaceDetails'])

if(len(response['FaceDetails']) > 0):
    res = client.search_faces_by_image(
        CollectionId = CollectionId,
        Image={
            'Bytes' : file
        }
    )
    print("There is this face in the database.")
    print(res['FaceMatches'])
else:
    print("No Faces detected in Input Image.")
