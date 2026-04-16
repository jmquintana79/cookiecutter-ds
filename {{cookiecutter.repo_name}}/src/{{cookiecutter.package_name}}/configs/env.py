""" 
Main folders root-folder definition (project, data, logs, outputs)

Normally data, outputs and logs folders are inside of folder project.
However it is not true always. For this reason I give the possibility
to define them individualy.
"""
import os
from pathlib import Path

# project folder
FOLDER_PROJECT = Path(os.environ.get("PROJECT_ROOT", os.getcwd()))
FOLDER_DATA = r""


def main():
    print(f'[info] project folder: "{FOLDER_PROJECT}"')

if __name__ == "__main__":
    main()