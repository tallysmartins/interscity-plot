#!/usr/bin/env python

import argparse
import glob
import os
import sys
import graphics as graphics
import project as project

__version__ = '0.0.1'

AVAILABLE_COMMANDS = ['start', 'delete', 'show', 'describe']

def _clear_cache():
    for cache in glob.iglob('{0}*'.format(CACHE_FILE)):
        os.remove(cache)

def _args_parser():
    parser = argparse.ArgumentParser(description='Plot and analyse traffic simulations from InterSCimulator')
    subparsers = parser.add_subparsers(title='Command', dest='command', help='The command to be run')

    parser.add_argument('-v', '--version', help='displays the current version of interscityplot',
                        action='store_true')
    project.adds_parser_args(subparsers)
    return parser

def cli_runner():
    parser = _args_parser()
    args = vars(parser.parse_args())
    cmd = args['command']

    if args['version']:
        print('InterscityPlot version (%s)' % __version__)
        return

    if cmd == None or cmd == [] or not cmd in AVAILABLE_COMMANDS:
        parser.print_help()
        return

    if os.getenv('INTERSCITY_PLOT_PROJECT'):
        args['project'] = os.getenv('INTERSCITY_PLOT_PROJECT')

    interscityplot(cmd, args)

def interscityplot(cmd, args):
    if cmd == 'show':
        graphics.run(args)
    else:
        project.run(cmd, args)

if __name__ == '__main__':
    cli_runner()
