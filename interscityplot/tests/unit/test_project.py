import pytest

from ..test_helper import *
from interscityplot.project import *

class TestProject(object):
    project_name = 'Project1'
    datasets = 'Project1/datasets'
    csv = 'mycsv.csv'


    """
    def process_dataset(self) -> None
    """
    def test_project_should_have_status_processed_equal_to_true(self):
        project = Project(self.project_name, self.csv)

        assert project.processed == None
        project.process_dataset()
        assert project.processed

    def test_should_return_number_of_pipelines_processed(self):
        project = Project(self.project_name, self.csv)
        assert 1 == project.process_dataset()


    """
    def create_project_files(self) -> None
    """
    def test_should_should_be_able_to_create_project_files(self):
        assert not path.isdir(self.project_name)

        project = Project(self.project_name, self.csv)
        project.create_project_files()

        assert path.isdir(self.project_name)
        assert path.isdir(self.datasets)

        # cleaning
        delete_folder(self.project_name)

    def test_should_return_proper_error_when_project_already_exists(self):
        project = Project(self.project_name, self.csv)
        project.create_project_files()

        with pytest.raises(Exception) as e:
            project.create_project_files()

        assert 'already exist' in str(e.value)
        Project.delete(self.project_name)

    def test_should_return_proper_error_when_user_has_no_permissions(self):
        project = Project('/' + self.project_name, self.csv)

        with pytest.raises(Exception) as e:
            project.create_project_files()

        assert 'No permission to create project' in str(e.value)

    """
    def delete(self, name: str) -> None:
    """
    def test_should_delete_project_folder(self):
        project = Project(self.project_name, self.csv)
        project.create_project_files()

        assert path.isdir(self.project_name)
        Project.delete(self.project_name)
        assert not path.isdir(self.project_name)

    def test_should_return_proper_error_when_deleting_an_inexistent_project(self):
        assert not path.isdir('xablau')

        with pytest.raises(Exception) as e:
            Project.delete('xablau')

        assert 'not found, please check the project name' in str(e.value)
