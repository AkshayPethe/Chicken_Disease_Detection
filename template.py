#This is a Basic Template for the Project as to Run and Automatically Create a Project File Structures.
import os
from pathlib import Path
import logging

#Logging is to Log The Basic Info for the activity with Format as Asctime: Current Time with Message
logging.basicConfig(level = logging.INFO,format='[%(asctime)s] :%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

project_name = "cnnClassifier"

list_file = [
    ".github/workflows/.gitkeep",#This is used in various task (.gitkeep) is made to let it empty
    f"src/{project_name}/__init__.py", #__init__.py is used to import any file as module
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py", # Used for reusable code
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml", #For MLOps Tool
    "params.yaml", #All the parameters will be controlled from this file
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

#We will Make path for each components of the List File
for filepath in list_file:
   
    filepath = Path(filepath)  # As Windows env follows Backward Slash we need to Change it by Path fn 

    

    filedir,filename = os.path.split(filepath) # We need to Seperate the Folder and File components.

    if filedir !="":      #Check if Filedir is not empty
        #
        os.makedirs(filedir, exist_ok = True)  #Make Directory if it doesn't exist or ensures it doesn't raise an error if the directory already exists
        logging.info(f"Creating Directory for {filename}")
    
   
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):  # #checks if the file doesn't exist or has a size of 0.

              
        with open(filepath,"w") as f: # #opens the file in write mode, creating it if it doesn't exist, and immediately closes it 
            pass
            logging.info("Creating Empty File : {filepath}")

    else:
        logging.info(f"{filename} already exists")





