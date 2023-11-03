from Chicken_Disease_Classification.config.configuration import ConfigurationManager
from Chicken_Disease_Classification import logger
from Chicken_Disease_Classification.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} initialised <<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e