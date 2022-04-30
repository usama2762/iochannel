__version__ = '0.1'
import json

import boto3

from iochannel.config import S3_BUCKET, S3_KEY_PREFIX


class IOChannel:
    def __init__(self):
        self.s3 = boto3.resource('s3')

    def read_input(self, request_id, **kwargs):
        obj = self.s3.Object(S3_BUCKET, f'{request_id}/input.json')
        data = json.load(obj.get()['Body'])
        return data

    def write_output(self, request_id, output, **kwargs):
        object_name = f'{S3_KEY_PREFIX}{request_id}/output.json'
        self.s3.Bucket(S3_BUCKET).upload_file(output, object_name)
        return object_name
