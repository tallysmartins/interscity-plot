import argparse
import os, pathlib
import pandas as pd
import shutil
from typing import Dict

class Project():
    def __init__(self, name: str, input_csv: str, nrows: int) -> object:
        """
        Initialize new project class with following attributes
        :param name:
        :param input_csv: csv file containing the simulation dataset
        :param nrows: integer value to be used as sample size of the dataset
        """
        self.name = name
        self.input_csv = input_csv
        self.nrows = nrows
        self.processed = None
        self.create_project_files()


    def run(self):
        self.process_dataset()
        self.save()

    def process_dataset(self):
        print("Processing dataset . . . .")

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
            raise Exception("Oops! Looks like a project called '%s' already exists in this folder" % name)
        except Exception as e:
            raise e

    def load_project(self, name: str) -> object:
        """
        Load project data from its directory
        """
        pass

    @classmethod
    def delete(self, name: str) -> None:
        """
        Clean up all project files
        :param name: Project name matching the project folder name
        """
        try:
            shutil.rmtree(name)
            print("Project deleted!" % name)
        except Exception as e:
            print(e)


############################################################################
# Command line arguments and commands
############################################################################

def run(cmd: str, args: Dict) -> None:
    if cmd == 'start':
        name, csv_file, nrows = get_project_attrs_from_args(args)
        project = Project(name, csv_file, nrows)
        project.run()
    elif cmd == 'delete':
        name, _csv_file, _nrows = get_project_attrs_from_args(args)
        Project.delete(name)
    else:
        print("Command '%s' not implemented!" % cmd)
        pass


def is_csv(file_path: str) -> bool:
    is_file = os.path.isfile(file_path)
    file_extension = pathlib.Path(file_path).suffix

    return is_file and '.csv' in file_extension


def get_project_attrs_from_args(args):
    return args.get('name'), args.get('file'), args.get('sample')

def adds_parser_args(subparsers):
    adds_start_command(subparsers)
    adds_delete_command(subparsers)

def adds_start_command(subparsers):
    usage = 'interscity-plot start myproject my_data.csv'
    parser = subparsers.add_parser('start', help='Start new project', usage=usage)
    parser.add_argument('name', metavar='NAME', type=str,
                        help='name of the new project')

    parser.add_argument('file', metavar='CSV_FILE', type=str,
                        help='output csv file containing the simulation data')

    parser.add_argument('--sample', metavar='INT', type=int, required=False,
                        help='value to define a sample size from the full dataset')
    return

def adds_delete_command(subparsers):
    usage = 'interscity-plot delete myproject'
    parser = subparsers.add_parser('delete', help='Delete existent project')
    parser.add_argument('name', metavar='NAME', type=str,
                        help='project name')
