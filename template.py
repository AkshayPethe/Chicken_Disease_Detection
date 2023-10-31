import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
#asctime is the current time for logging

project_name = "Chicken Disease Classification"

list_of_files = [
    ".github/workflows/.gitkeeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils.py/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    


]

for filepath in list_of_files:
    #As we are operating in Windows,Path will change forward Slash to Backword Slash are required by Windows Config
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)  

    if filedir != "":
        os.makedirs(filedir,exist_ok = True)
        logging.info(f"Creating Directory {filedir} for {filename} ")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} already exist")
