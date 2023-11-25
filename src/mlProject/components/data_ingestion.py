import os
from mlProject import logger
from mlProject.utils.common import get_size
import boto3
from pathlib import Path
from mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion():
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def get_file(self):
        if not os.path.exists(self.config.local_data_file):
            s3 = boto3.client('s3')
            s3 = boto3.resource(
                service_name='s3',
                region_name='us-east-1',
                aws_access_key_id = '',
                aws_secret_access_key = ''
            )
            for obj in s3.Bucket('vedanshaws').objects.all():
                filename = obj.key
            
            s3.Bucket('vedanshaws').download_file(Key='winequality-red.csv', Filename=self.config.download_dir)
            logger.info(f"{filename} downloaded from S3 bucket!")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            