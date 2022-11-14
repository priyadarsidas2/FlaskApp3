import boto3
import os
from datetime import date

access_key = "AKIAXDGEK2YNKWIEE3KW"
secret_key = "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"

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_key)

def uploadFileToS3(filename):
    upload_file_bucket = 'resume-demo-s3'
    dateTodayRaw = date.today()
    dateToday = dateTodayRaw.strftime("%d/%m/%Y")
    dateToday = dateToday.replace("/", "-")
    upload_file_key = dateToday + "/" + str(filename)
    
    client.upload_file(filename, upload_file_bucket, upload_file_key)
    #file_url = '%s/%s/%s' % (client.meta.endpoint_url, upload_file_bucket, upload_file_key)
    file_url = "https://resume-demo-s3.s3.ap-south-1.amazonaws.com/" + dateToday + "/" + filename.replace(" ", "+")
    print("File Uploaded")
    return (file_url, dateToday)