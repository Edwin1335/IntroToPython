from urllib.parse import unquote_plus
import json
import boto3
import extract_msg
import os
import sys
import uuid
import re


# import pandas as pd
# import io
##import xlrd


def lambda_handler(event, context):
    # The event object will have info. We're getting the bucket, key, and tmpkey
    bucket = event['Records'][0]['s3']['bucket'][
        'name']  # Our original bucket. It's grabbing the event for us (we already mentioned which bucket). If you have multiple bucket, it will run a lambda function for each bucket.
    key = unquote_plus(event['Records'][0]['s3']['object'][
                           'key'])  # Grabs the key that was assigned to the file by s3 originally (every key is prefixed with all the folder names)
    tmpkey = key.replace('/', '')  # removes every slash in the tmpkey, we want to remove it
    s3_client = boto3.client(
        's3')  # Creating a client object that will help us interface with s3, it contains boiler plate code to interact with s3. Called the boto3 library.
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)  # path to the invisible folder that contains the files
    s3_client.download_file(bucket, key, download_path)
    # img_lambda(bucket, key)     #should pass download_path instead of bucket and key
    # print(download_path)
    # excel_lambda(bucket, key)
    # downloading the actual file from s3 into a local folder (that you can't see)
    msg = extract_msg.openMsg(download_path)
    msg_sender = msg.sender
    msg_date = msg.date
    msg_subj = msg.subject
    msg_message = msg.body
    msg.save_attachments(customPath="/tmp/")
    searchRegex(msg_subj)
    print(f"Printing Body: {msg_message}")
    print(f"Serial NUmber: {extractSN(msg_message)}")

    put_email(extractSN(msg_message), msg_subj)

    # Create an array later for multiple attachments. So far, this works for a single attachment
    # msg_attachment = "/tmp/" + msg.attachments #This should be a list of attachments (it only returns their names)
    # print(msg.attachments)
    #    get()
    # list(filter(os.path.isfile, os.listdir(<path>))) #"ls" command in linux but in python
    return {
        "statusCode": 200,
        # API endpoint (you must return a status code every time) (the default is 200) #I was missing a comma so it didn't work the first time
        "body": msg_message
    }


def put_email(serailNumber, subject):
    dynamodb = boto3.resource('dynamodb')
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    table = dynamodb.Table('EmailDataBase')
    response = table.put_item(
        Item={
            'SN': serailNumber,
            'Subject': subject,
        }
    )
    return response


def searchRegex(msg_subj):
    results = ""  # store SNs-- array?
    print(len(msg_subj))  # 1036 outputted for message, 63 chars for subj
    print(msg_subj)  # prints 1 line subj
    line = msg_subj.split()
    for word in line:
        print(word)


def extractSN(numbers):
    serialNumber = ""
    SList = []
    match = re.findall(r"\b[A-Z0-9]{7}\b|\b[A-Z0-9]{10}\b", numbers)
    for y in match:
        SList.append(y)

    if len(SList) > 1:
        closest = len(numbers)
        result = numbers.find('Serial', 0, len(numbers))
        if result == -1:
            result = numbers.find('SN', 0, len(numbers))
        if result == -1:
            result = numbers.find('S/N', 0, len(numbers))
        if result == -1:
            result = numbers.find('org_serial_no', 0, len(numbers))

        for i in range(result, len(numbers)):
            for matches in SList:
                if numbers.find(matches) <= closest and numbers.find(matches) > result:
                    closest = numbers.find(matches)

        for x in range(closest, closest + 10):
            serialNumber = serialNumber + numbers[x]

    # testing SList and serialNumber
    # print(serialNumber)
    # print('\n', SList)
    return serialNumber


"""
def img_lambda(bucket, document):           #no need for upload path, download_path definitely
    #bucket = event['Records'][0]['s3']['bucket']['name']           
    #document = "document"
    client = boto3.client('textract')
    response = client.detect_document_text( Document = {'S3Object': {'Bucket': bucket, 'Name': document}})          #sending s3 obj address, can change and send bytes
    blocks = response['Blocks']         #Get the text blocks
    return {
        "statusCode": 200,
        "body": json.dumps(blocks)
    }


def excel_lambda(bucket, document):         #pass bucket and key from handler
    client = boto3.client('s3')
    file_obj = client.get_object(Bucket= bucket, Key= document)
    file_content = file_obj["Body"].read()
    #excelFile = io.BytesIO(file_content)

    df = pd.read_excel(excelFile)
    print(df)
    return {
        "statusCode": 200,
        #"body": json.dumps(blocks)
    }
"""