# InterSCityPlotter

[![Build Status](https://travis-ci.org/tallysmartins/interscity-plot.svg?branch=master)](https://travis-ci.org/tallysmartins/interscity-plot)
[![License](https://img.shields.io/cran/l/devtools.svg)](https://github.com/tallysmartins/interscity-plot/blob/master/LICENSE)

Plot and analyse traffic simulations from the InterSCimulator

## Features

- Plot vehicles dots
- Plot vehicles graph
- Plot vehicles density

## Installation and Usage

InterSCityPlotter was built with Python 3.6 and no other version was tested. To have
it, simple clone this repository and run

	$ python3 setup.py

This will install and load all the modules to your environment. The following
commands and flags are available:

    usage: interscity-plot [-h] [-v] {start,delete} ...

    Plot and analyse traffic simulations from InterSCimulator

    optional arguments:
      -h, --help      show this help message and exit
      -v, --version   displays the current version of interscityplotter

    Command:
      {start,delete}  The command to be run
        start         Start new project
        delete        Delete existent project

## License

Project licensed under GPLv3

## Authors

- Tallys Martins
