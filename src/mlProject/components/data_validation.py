import os
from mlProject import logger
import boto3
from mlProject.entity.config_entity import Datavalidationconfig
import pandas as pd

class DataValidation():
    def __init__(self,config:Datavalidationconfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:

            validation_status = None

            s3 = boto3.client('s3')
            s3 = boto3.resource(
                service_name='s3',
                region_name='us-east-1',
                aws_access_key_id = '',
                aws_secret_access_key = ''
            )

            obj = s3.Bucket('vedanshaws').Object('winequality-red.csv').get()

            data = pd.read_csv(obj['Body'], index_col=0)
            all_columns = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"VALIDATION_STATUS : {validation_status}")

                else:
                    validation_status = True
                    with open(self.config.status_file,'w') as f:
                        f.write(f"VALIDATION_STATUS : {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e