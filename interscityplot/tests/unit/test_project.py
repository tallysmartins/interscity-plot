import pytest

from ..test_helper import *
from interscityplot.project import *


class SimplePipeline():
    def __init__(self, project):
        self.project = project
    def run(self):
        pass


class OtherSimplePipeline():
    def __init__(self, project):
        self.project = project
    def run(self):
        pass


class FailingPipeline():
    def __init__(self, project):
        self.project = project
    def run(self):
        raise Exception('This pipeline is broken')


class TestProject(object):
    project_name = 'Project1'
    datasets = 'Project1/datasets'
    csv = 'mycsv.csv'


    """
    def run(self) -> bool
    """
    def test_not_break_when_there_is_no_pipelines_to_be_run(self):
        project = Project(self.project_name, self.csv, pipelines=[])

        assert project.processed == None
        assert project.pipeline_runs == 0

        project.run()
        assert project.processed
        assert project.pipeline_runs == 0

    def test_should_run_simple_pipeline(self):
        project = Project(self.project_name, self.csv, pipelines=[SimplePipeline])

        assert project.processed == None
        assert project.pipeline_runs == 0

        project.run()
        assert project.processed
        assert project.pipeline_runs == 1

    def test_should_run_more_than_one_pipeline(self):
        project = Project(self.project_name, self.csv, pipelines=[SimplePipeline, OtherSimplePipeline])

        assert project.processed == None
        assert project.pipeline_runs == 0

        project.run()
        assert project.processed
        assert project.pipeline_runs == 2

    def test_should_catch_and_stop_when_pipeline_fails(self):
        project = Project(self.project_name, self.csv, pipelines=[SimplePipeline, FailingPipeline, OtherSimplePipeline])

        assert project.processed == None
        assert project.pipeline_runs == 0

        with pytest.raises(Exception) as e:
            project.run()

        assert not project.processed
        assert project.pipeline_runs == 1


    """
    def create_project_files(self) -> None
    """
    def test_should_should_be_able_to_create_project_files(self):
        assert not path.isdir(self.project_name)

        project = Project(self.project_name, self.csv)
        project.create_project_files()

        assert path.isdir(self.project_name)
        assert path.isdir(self.datasets)

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
