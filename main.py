from imageClassifier.pipeline.data_ingestion_v01 import DataIngestionTrainingPipeline
from imageClassifier import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage:1  {STAGE_NAME} started <<<<<<")
    
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    
    logger.info(f">>>>>> Stage:1  {STAGE_NAME} completed <<<<<<\n\n<========>")
except Exception as e:
    logger.exception(e)
    raise e