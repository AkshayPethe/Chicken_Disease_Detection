from Chicken_Disease_Classification.constants import *
from Chicken_Disease_Classification.utils.common import read_yaml, create_directories
from Chicken_Disease_Classification.entity.config_entity import DataIngestionConfig

#Making the Configuration manager to create a path by calling fn from common.py
class ConfigurationManager:
    """This class is designed to read configuration and parameter files from YAML files, 
    create necessary directories, and provide access to 
    specific configuration values."""
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # You may want to modify this line according to your actual directory structure
        create_directories([self.config.data_ingestion.root_dir])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])  # You should define create_directories

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
        
      