from mlProject import logger
from sklearn.model_selection import train_test_split
import os
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
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

        num_pipeline= Pipeline(
            steps=[
            ("imputer",SimpleImputer(strategy="median")),
            ("scaler",StandardScaler())

            ]
        )

        target_column_name="quality"
        numerical_columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
            'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
            'pH', 'sulphates', 'alcohol', 'quality']

        input_feature_train_df=train.drop(columns=[target_column_name],axis=1)
        target_feature_train_df=train[target_column_name]

        input_feature_test_df=test.drop(columns=[target_column_name],axis=1)
        target_feature_test_df=test[target_column_name]

        logger.info(
            f"Applying preprocessing object on training dataframe and testing dataframe."
        )

        input_feature_train_arr=num_pipeline.fit_transform(input_feature_train_df)
        input_feature_test_arr=num_pipeline.transform(input_feature_test_df)

        train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
        test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

        return(
            train_arr,
            test_arr,
        )
