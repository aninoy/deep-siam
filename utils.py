import os
import sys
import boto3


def get_raw_data():
    return data_download(filename='train.json')

def data_download(filename, data_dir='./data'):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    filepath = os.path.join(data_dir, filename)

    if not os.path.exists(filepath):
        region = boto3.Session().region_name
        boto3.Session().resource('s3', region_name=region).Bucket('deep-siam').download_file(filename, filepath)
    else:
        print("File already downloaded.")
    
    return data_dir
