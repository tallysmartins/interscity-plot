import argparse
import os, pathlib
import pandas as pd
import shutil
from typing import Dict, Tuple

class Summary():
    def __init__(self, project):
        self.project = project

    def run():
        print("Running Summary Pipeline")

class Project():
    """
    Initialize new project class with following attributes

    :param name:
    :param input_csv: csv file containing the simulation dataset
    :param nrows: integer value to be used as sample size of the dataset
    """
    def __init__(self, name: str, input_csv: str, nrows:int=None) -> object:
        self.name = name
        self.input_csv = input_csv
        self.nrows = nrows
        self.processed = None
        self.pipelines = [Summary]

    def run(self) -> None:
        self.process_dataset()
        self.save()

    def process_dataset(self) -> bool:
        print("Processing dataset . . . .")
        for index, pipeline in enumerate(self.pipelines):
            pipeline(self)
            pipeline.run()
        self.processed = True

        return index + 1

    def save(self):
        """
        Save project attributes to .meta file.
        """
        print("saving")

    def create_project_files(self) -> None:
        """
        Create project folder and sub files.
        Sub files created:
            - A datasets/ folder to store datasets after the pre processing
            - A .meta file to store project information and references
        """
        try:
            os.mkdir(self.name)
            os.mkdir(self.name + '/datasets')
        except FileExistsError as e:
            raise Exception("Oops! Looks like a project named '%s' already exists in this folder" % self.name)
        except PermissionError as e:
            raise Exception("No permission to create project files in this folder")
        except Exception as e:
            raise e

    @classmethod
    def delete(self, name: str) -> None:
        """
        Clean up all project files
        :param name: Project name matching the project folder name
        """
        try:
            shutil.rmtree(name)
            print("Project deleted!" % name)
        except FileNotFoundError as e:
            raise Exception("%s not found, please check the project name and try again" % name)
        except Exception as e:
            print(e)
