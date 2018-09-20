from interscityplot.project import Project

import os, pathlib
import shutil
from typing import Dict, Tuple

import pandas as pd
import argparse

def run(cmd: str, args: Dict) -> None:
    """
    Decide which command to run
    :param cmd: command to be run, supported commands are: (start, delete, describe)
    :param args: arguments read from the command line
    """
    try:
        if cmd == 'start':
            name, csv_file, nrows = get_attrs_from_args(args)
            project = Project(name, csv_file, nrows)
            project.run()
        elif cmd == 'delete':
            name, _csv_file, _nrows = get_attrs_from_args(args)
            Project.delete(name)
        else:
            print("Command '%s' not implemented!" % cmd)
            pass
    except Exception as e:
        print(e)

def get_attrs_from_args(args: Dict) -> Tuple:
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
