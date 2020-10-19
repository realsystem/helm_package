import boto3
import logging
from botocore.exceptions import ClientError

DEFAULT_REGION = 'us-east-1'

# Amazon Linux 2
IMAGE_ID = 'ami-0603cbe34fd08cb81'


class MyTerra:
    def __init__(self, region):
        if len(region) != 0:
            self.region = region
        else:
            self.region = DEFAULT_REGION
        self.session = boto3.Session(region_name=self.region)
        self.s3_client = self.session.client('s3')
        self.s3_resource = boto3.resource('s3')

    def check_status(self, bucket_name, object_name):
        s3_object = self.s3_resource.Object(bucket_name, object_name)
        try:
            response = s3_object.get()
            logging.debug(msg=response)
        except ClientError as e:
            logging.error(e)
            if e.response['Error']['Code'] == 'NoSuchKey':
                return e.response['Error']['Message']
        return 'uploaded'

    def create_download_url(self, bucket_name, object_name, expiration=3600):
        try:
            response = self.s3_client.generate_presigned_url('get_object',
                                                             Params={'Bucket': bucket_name,
                                                                     'Key': object_name},
                                                             ExpiresIn=expiration)
            logging.debug(msg=response)
        except ClientError as e:
            logging.error(e)
            return None

        return response

    def create_upload_url(self, bucket_name, object_name, fields=None, conditions=None, expiration=3600):
        try:
            response = self.s3_client.generate_presigned_post(bucket_name,
                                                              object_name,
                                                              Fields=fields,
                                                              Conditions=conditions,
                                                              ExpiresIn=expiration)
            logging.debug(msg=response)
        except ClientError as e:
            logging.error(e)
            return None

        return response
