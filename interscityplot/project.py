import argparse
import os, pathlib
import pandas as pd


def run(cmd, args):
    if cmd == 'start':
        name, csv_file, nrows = get_project_attrs_from_args(args)
        start_project(name, csv_file, nrows)
    else:
        print("Command '%s' not implemented!" % cmd)
        pass

def start_project(name, input_csv, nrows):
    """
    Create new project folder from a given dataset and sample size
    :param name:
    :param input_csv: csv file containing the simulation dataset
    :param nrows: integer value to be used as sample size of the dataset
    """
    print("Project '%s' created!" % name)
    pass


def create_project_files(name):
    try:
        os.mkdir(name)
        os.mkdir(name+'/datasets')
    except Exception as e:
        raise e("A Problem occurred when setting up project files")
    
def is_csv(file_path):
    is_file = os.path.isfile(file_path)
    file_extension = pathlib.Path(file_path).suffix

    return is_file and '.csv' in file_extension

############################################################################
# Command line arguments and commands
############################################################################
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
    parser.add_argument('name', metavar='NAME', type=str, nargs='*',
                        help='project name')
