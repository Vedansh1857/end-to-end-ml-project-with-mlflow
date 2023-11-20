from mlProject.config.configuration import ConfigurationManager
from mlProject.entity.config_entity import DataIngestionConfig
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger

STAGE_NAME = 'Data ingestion stage'

class DataIngestionTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.get_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e
