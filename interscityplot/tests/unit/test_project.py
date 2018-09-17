from ..test_helper import *
from ...project import *
import pytest
import os.path as path

"""
def is_csv(file_path)
"""
def test_return_true_if_file_is_csv():
    assert is_csv(path.abspath('./tests/fixtures/simulation.csv'))

def test_return_false_if_file_is_not():
    assert not is_csv('./tests/fixtures/simulation.txt')

def test_return_false_if_file_does_not_exist():
    assert not is_csv('./tests/fixtures/abadubada.shine')

"""
def create_project_files(name)
"""
def test_create_project_files_given_project_name(): 
    project_name = 'Project1'
    datasets = 'Project1/datasets'

    assert not path.isdir(project_name)

    create_project_files(project_name)

    assert path.isdir(project_name)
    assert path.isdir(datasets)

    # cleaning
    delete_folder(project_name)

