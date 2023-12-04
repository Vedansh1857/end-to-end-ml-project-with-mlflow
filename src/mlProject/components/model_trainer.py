import os
from mlProject import logger
import joblib
import pandas as pd
from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from sklearn.ensemble import RandomForestClassifier
from mlProject.config.configuration import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # obj1 = ConfigurationManager()
        cfg = ConfigurationManager().get_data_transformation_config()
        # obj2 = DataTransformation(config=cfg)
        train_arr,test_arr = DataTransformation(config=cfg).train_test_splitting()

        x_train,y_train,x_test,y_test = (
            train_arr[:,:-1],
            train_arr[:,-1],
            test_arr[:,:-1],
            test_arr[:,-1]
        )

        # x_train = train_data.drop([self.config.target_column], axis=1)
        # x_test = test_data.drop([self.config.target_column], axis=1)
        # y_train = train_data[[self.config.target_column]]
        # y_test = test_data[[self.config.target_column]]
        
        rfc = RandomForestClassifier(criterion=self.config.criterion, n_estimators=self.config.n_estimators, random_state=42)
        rfc.fit(x_train,y_train)

        joblib.dump(rfc,os.path.join(self.config.root_dir,self.config.model_name))