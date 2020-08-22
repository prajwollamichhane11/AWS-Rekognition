import boto3
import base64

aws_access_key_id = "##############"
aws_secret_access_key = "##############"
aws_session_token = "##############"


client = boto3.client('rekognition', aws_session_token=aws_session_token, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name="us-east-1")

file = open('img4.jpeg','rb').read()

CollectionId = "GeneseCollection"


response = client.index_faces(
    CollectionId = CollectionId,
    Image = {
        'Bytes' : file
    },
    ExternalImageId = "DayaHangRai" #Dont Give Spaces on names
)
print(response)
