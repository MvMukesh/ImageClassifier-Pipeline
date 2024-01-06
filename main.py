from imageClassifier import logger
from imageClassifier.pipeline.data_ingestion_v01 import DataIngestionTrainingPipeline
from imageClassifier.pipeline.modelPrep_base_v02 import PrepareBaseModelTrainingPipeline
from imageClassifier.pipeline.training_v03 import ModelTrainingPipeline



#1
STAGE_NAME = "Data Ingestion | Stage-1"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\n<========>")
except Exception as e:
    logger.exception(e)
    raise e

#2
STAGE_NAME = "Base Model Prep | Stage-2"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

#3
STAGE_NAME = "Training Model | Stage-3"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

# #4
# STAGE_NAME = "Evaluation | Stage-4"
# try:
#    logger.info(f"*******************")
#    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#    model_evalution = EvaluationPipeline()
#    model_evalution.main()
#    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e