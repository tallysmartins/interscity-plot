#!/usr/bin/env python

#System imports
import glob
import os
import sys

# Third part imports
import argparse

# Local imports
from . import project_cli as project

__version__ = '0.0.1'

AVAILABLE_COMMANDS = ['start', 'delete', 'show', 'describe']

def args_parser():
    parser = argparse.ArgumentParser(description='Plot and analyse traffic simulations from InterSCimulator')
    subparsers = parser.add_subparsers(title='Command', dest='command', help='The command to be run')

    parser.add_argument('-v', '--version', help='displays the current version of interscityplot',
                        action='store_true')

    project.adds_parser_args(subparsers)
    return parser

def override_args_from_env(args):
    if os.getenv('INTERSCITY_PLOT_PROJECT'):
        args['project'] = os.getenv('INTERSCITY_PLOT_PROJECT')

    return args

def run_command():
    parser = args_parser()
    args = vars(parser.parse_args())
    cmd = args['command']

    if args['version']:
        print('InterscityPlot version (%s)' % __version__)
        return

    args = override_args_from_env(args)
    project.run(cmd, args)

if __name__ == '__main__':
    run_command()
