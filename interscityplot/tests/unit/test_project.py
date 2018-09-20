import pytest

from ..test_helper import *
from interscityplot.project import *

class TestProject(object):
    project_name = 'Project1'
    datasets = 'Project1/datasets'
    csv = 'mycsv.csv'

    def test_should_should_be_able_to_create_project_files(self): 
        assert not path.isdir(self.project_name)

        project = Project(self.project_name, self.csv)
        project.create_project_files()

        assert path.isdir(self.project_name)
        assert path.isdir(self.datasets)

        # cleaning
        delete_folder(self.project_name)

    def test_should_return_error_when_project_already_exists(self):
        project = Project(self.project_name, self.csv)
        project.create_project_files()

        with pytest.raises(Exception): 
            project.create_project_files()

        delete_folder(self.project_name)
