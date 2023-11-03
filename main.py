from src.Chicken_Disease_Classification import logger
from Chicken_Disease_Classification.pipeline.S01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} initialised <<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

