from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataTransformationConfig
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger

STAGE_NAME = 'Data transformation stage'

class DataTransformationTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e