#!/usr/bin/env python3

from setuptools import setup, find_packages
import howdoi
import os

def extra_dependencies():
    import sys
    return ['argparse'] if sys.version_info < (2, 7) else []


def read(*names):
    values = dict()
    for name in names:
        value = ''
        for extension in ('.txt', '.rst'):
            filename = name + extension
            if os.path.isfile(filename):
                with open(filename) as in_file:
                    value = in_file.read()
                break
        values[name] = value
    return values


long_description = """
%(README)s
""" % read('README')

setup(
    name='interscityplot',
    version=interscityplot.__version__,
    description='Plot and analyse traffic simulations from InterSCimulator',
    long_description=long_description,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers, Data Scientists",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='interscity visualization traffic simulation smart cities',
    author='Tallys Martins',
    author_email='tallys@ime.usp.br',
    maintainer='Tallys Martins',
    maintainer_email='tallys@ime.usp.br',
    url='https://github.com/tallysmartins/interscity-plot',
    license='GPLv3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'interscity-plot = interscityplot.interscityplot:cli_runner',
        ]
    },
    install_requires=[
        'pygments',
        'pandas',
        'matplotlib',
        'geoplotlib',
        'pyglet',
        'scipy',
    ] + extra_dependencies(),
)
