import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="CNN CLASSIFIER"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
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
    "research/trails.ipynb",
    "template/index.html",


]

for path in list_of_files:
    path=Path(path)
    dir, file_name=os.path.split(path)

    if dir !="":
        os.makedirs(dir, exist_ok=True)
        logging.info(f"creating directory: {dir} for the file: {file_name}")
    
    if (not os.path.exists(path)) or (os.path.getsize(path)==0):
        with open(path, "w") as f:
            pass
            logging.info(f"creating empty file: {path}")
    else:
        logging.info(f"{file_name} is already exists")
