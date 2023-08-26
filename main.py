
from texttranslation.logging import logger
from texttranslation.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from texttranslation.pipeline.stage02_data_validation import DataValidationTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f"{STAGE_NAME} Started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"{STAGE_NAME} Started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e