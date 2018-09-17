from ..test_helper import *
from ... import interscityplot

def test_start_project_given_name_and_input_data():
    interscityplot.interscityplot('start', {'name': 'my project'})
    assert 3 == 3

def not_a_test():
    print("not a test")
    pass
