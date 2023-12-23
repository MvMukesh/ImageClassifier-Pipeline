from imageClassifier import logger
from imageClassifier.pipeline.data_ingestion_v01 import DataIngestionTrainingPipeline
from imageClassifier.pipeline.modelPrep_base_v02 import PrepareBaseModelTrainingPipeline


#1
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage:1  {STAGE_NAME} started <<<<<<")
    
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    
    logger.info(f">>>>>> Stage:1  {STAGE_NAME} completed <<<<<<\n\n<========>")
except Exception as e:
    logger.exception(e)
    raise e

#2
STAGE_NAME = "Model Prep Base"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

