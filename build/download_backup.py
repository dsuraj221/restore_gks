import boto3
import botocore
import os
from zipfile import ZipFile

BUCKET_NAME = os.environ['bucket_name']
KEY = os.environ['back_up_file']


def download_from_s3():
    s3 = boto3.resource('s3')

    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise


def unzip_backup():
    file_name = os.environ['back_up_file']
    zf = ZipFile(file_name, 'r')
    zf.extractall()
    zf.close()


download_from_s3()
unzip_backup()