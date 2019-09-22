import boto3
s3 = boto3.client('s3')
s3.download_file('manujabucket1', 'file1', 'file2')

#---using botocore---------

import boto3
import botocore

s3 = boto3.resource('s3')
try:
    s3.Bucket('manujabucket1').download_file('file1', 'file2')
except botocore.exceptions.ClientErrors as e:
    if e.response['Error']['Code'] == '404':
        print('Files does not exist')
    else:
        raise