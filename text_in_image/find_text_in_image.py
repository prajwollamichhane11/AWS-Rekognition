import boto3
import base64


aws_access_key_id = "##############"
aws_secret_access_key = "##############"
aws_session_token = "##############"

client = boto3.client('rekognition', aws_session_token=aws_session_token, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name="us-east-1")

file = open('speed.png','rb').read()

response = client.detect_text(
    Image={
        "Bytes" : file
    }
)

# print(response['TextDetections'])
texts = []

for text in response['TextDetections']:
    if(text['Type'] == "WORD"):
        texts.append(text["DetectedText"])

strTexts = " ".join(texts)

print("----------------------------------------")
print(strTexts)
print("----------------------------------------")