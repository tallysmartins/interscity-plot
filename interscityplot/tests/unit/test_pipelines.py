import pytest

from ..test_helper import *
from interscityplot.pipelines import SummaryStats
from interscityplot.project import Project

class TestSummaryStats():

    """
    def init(self, project)
    """
    def test_initialize_with_correct_attributes(self):
        project = Project('myproject', 'mycsv', nrows=10)
        pipeline = SummaryStats(project)
        assert pipeline.csv == 'mycsv'
        assert pipeline.nrows == 10
        assert pipeline.dest_dir == 'myproject'
        assert pipeline.metrics == {}
        assert pipeline.data == None


    """
    def load_dataset(self):
    """
    def test_return_dataframe_from_loaded_csv(self):
        csv = fixtures_dir + '/simulation.csv'
        df = SummaryStats.load_dataset(csv)
        columns = ['time', 'action', 'vid', 'lat', 'lon']

        assert 'DataFrame' in df.__class__.__name__
        assert df.size > 1
        assert any(df.columns.values == columns)

    def test_raise_if_if_loading_fails(self):
        with pytest.raises(Exception) as e:
            df = SummaryStats.load_dataset('anything.csv')
