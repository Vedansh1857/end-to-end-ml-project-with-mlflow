from mlProject import logger
from sklearn.model_selection import train_test_split
import os
import pandas as pd
import numpy as np
from sklearn.utils import resample
from mlProject.config.configuration import DataTransformationConfig

class DataTransformation():
    def __init__(self,config:DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        
        data = pd.read_csv(self.config.data_path)

        ## Treating outliers below...
        def log_transform(col):
            return np.log(col[0])

        data['residual sugar'] = data[['residual sugar']].apply(log_transform, axis=1)
        data['chlorides'] = data[['chlorides']].apply(log_transform, axis=1)
        data['free sulfur dioxide'] = data[['free sulfur dioxide']].apply(log_transform, axis=1)
        data['total sulfur dioxide'] = data[['total sulfur dioxide']].apply(log_transform, axis=1)
        data['sulphates'] = data[['sulphates']].apply(log_transform, axis=1)

        ## Handling imbalanced dataset below...
        df_3 = data[data.quality==3]     # MINORITY
        df_4 = data[data.quality==4]     # MINORITY
        df_5 = data[data.quality==5]     # MAJORITY
        df_6 = data[data.quality==6]     # MAJORITY
        df_7 = data[data.quality==7]     # MINORITY
        df_8 = data[data.quality==8]     # MINORITY

        # Oversample MINORITY Class to make balance data :
        df_3_upsampled = resample(df_3, replace=True, n_samples=600, random_state=12) 
        df_4_upsampled = resample(df_4, replace=True, n_samples=600, random_state=12) 
        df_7_upsampled = resample(df_7, replace=True, n_samples=600, random_state=12) 
        df_8_upsampled = resample(df_8, replace=True, n_samples=600, random_state=12) 
        # Decreases the rows of Majority one's to make balance data :
        df_5_downsampled = data[data.quality==5].sample(n=600).reset_index(drop=True)
        df_6_downsampled = data[data.quality==6].sample(n=600).reset_index(drop=True)
        # Combine downsampled majority class with upsampled minority class
        Balanced_df = pd.concat([df_3_upsampled, df_4_upsampled, df_7_upsampled, df_8_upsampled, df_5_downsampled, df_6_downsampled]).reset_index(drop=True) 

        train, test = train_test_split(Balanced_df,test_size=0.2,random_state=42)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index=False,header=True)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index=False,header=True)

        logger.info("Splitted the data into test & training data")
        logger.info(f"Shape of the training data is : {train.shape}")
        logger.info(f"Shape of the test data is : {test.shape}")

        print(train.shape)
        print(test.shape)

        ''' Scaling the data'''
        # num_pipeline= Pipeline(
        #     steps=[
        #     ("imputer",SimpleImputer(strategy="median")),
        #     ("scaler",MinMaxScaler())
        #     ]
        # )

        # target_column_name="quality"

        # input_feature_train_df=train.drop(columns=[target_column_name],axis=1)
        # target_feature_train_df=train[target_column_name]

        # input_feature_test_df=test.drop(columns=[target_column_name],axis=1)
        # target_feature_test_df=test[target_column_name]

        # logger.info(
        #     f"Applying preprocessing object on training dataframe and testing dataframe."
        # )

        # input_feature_train_arr=num_pipeline.fit_transform(input_feature_train_df)
        # input_feature_test_arr=num_pipeline.fit_transform(input_feature_test_df)

        # train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
        # test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

        # return(
        #     train_arr,
        #     test_arr,
        # )
