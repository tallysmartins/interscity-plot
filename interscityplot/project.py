import shutil
import os, pathlib
from typing import Dict, Tuple

import argparse
import pandas as pd
from . pipelines import SummaryStats

class Project():
    """
    Initialize new project class with following attributes

    :param name: name of the project (also used as the project folder name)
    :param input_csv: csv file containing the simulation dataset
    :param nrows: integer value to be used as sample size of the dataset
    """
    def __init__(self, name: str, input_csv: str, nrows:int=None, pipelines=[]) -> object:
        self.name = name
        self.input_csv = input_csv
        self.nrows = nrows
        self.processed = None
        self.pipeline_runs = 0
        self.pipelines = set(pipelines)
        self.datasets_dir = self.name + '/datasets'

    def run(self) -> bool:
        self.pipeline_runs = 0
        for pipeline in self.pipelines:
            try:
                pipeline(self).run()
                self.pipeline_runs += 1
            except Exception as e:
                print("\nError executing the '%s' pipeline" % pipeline.__name__)
                raise e

        self.processed = True

    def add_pipeline(self, pipeline):
        self.pipelines.add(pipeline)

    def remove_pipeline(self, pipeline):
        self.pipelines.discard(pipeline)

    def create_project_files(self) -> None:
        """
        Create project folder and sub files.
        Sub files created:
            - A datasets/ folder to store datasets after the pre processing
            - A .meta file to store project information and references
        """
        try:
            os.mkdir(self.name)
            os.mkdir(self.datasets_dir)
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
