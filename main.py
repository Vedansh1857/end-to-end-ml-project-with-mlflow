from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = 'Data ingestion stage'

try:
    logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data validation stage'

try:
    logger.info(f">>>>>>>> Stage : {STAGE_NAME} started <<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> Stage : {STAGE_NAME} completed <<<<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data transformation stage'

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e