import os
from box.exceptions import BoxValueError
import yaml
from Chicken_Disease_Classification import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations  
def get_size(path: Path) -> str:
    """Get the size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size in KB as a formatted string.
    """
    try:
        size_in_bytes = os.path.getsize(path)
        size_in_kb = round(size_in_bytes / 1024)
        return f"~{size_in_kb} KB"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        logger.error(f"Error getting file size: {str(e)}")
        return "Error"