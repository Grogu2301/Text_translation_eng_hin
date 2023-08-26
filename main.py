
from texttranslation.logging import logger
from texttranslation.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f"{STAGE_NAME} Started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e