import os;
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

package_name = "deepClassifier"

list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/init/__init__.py",
    f"src/{package_name}/component/__init__.py",
    f"src/{package_name}/util/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirement_dev.txt",
    "setup.py",
    "pyproject.toml",
    "tox.ini",
    "reserch/trails.ipynb"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Create directory : {filedir} for file: {filename}")

    if(not os.path.exists(filepath) or (os.path.getsize(filepath))):
        with open(filepath, "w") as f:
            pass # create empty file
            logging.info(f"Create directory : {filedir}")
    else:
        logging.info(f"{filename} : file already exists")

    