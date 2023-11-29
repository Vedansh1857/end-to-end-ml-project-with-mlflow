from mlProject import logger
from sklearn.model_selection import train_test_split
import os
import pandas as pd
from mlProject.config.configuration import DataTransformationConfig

class DataTransformation():
    def __init__(self,config:DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data,test_size=0.2,random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index=False,header=True)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index=False,header=True)

        logger.info("Splitted the data into test & training data")
        logger.info(f"Shape of the training data is : {train.shape}")
        logger.info(f"Shape of the test data is : {test.shape}")

        print(train.shape)
        print(test.shape)