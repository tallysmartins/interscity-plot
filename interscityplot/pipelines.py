import json
from typing import Dict

import pandas as pd

class SummaryStats():
    """
        SummaryStats pipeline calculate basic metrics from a dataset of a project.
        The dataset passes through a cleaning step where unfinished trips are
        removed from the dataset. Unfinished trips are considered those ones that
        misses the 'arrival' entry, this may happen when a sampling of the simulation
        is used.

        Take the following dataset:
           time  action         vid          lon            lat
        1)  25;  start;      4858_52;    -23.624235;    -46.648388
        2)  27;  start;      4858_73;    -23.624235;    -46.648388
        3)  31;  move;       4858_52;    -23.624077;    -46.648453
        4)  33;  move;       4858_73;    -23.624077;    -46.648453
        5)  47;  move;       4858_52;    -23.624277;    -46.648983
        6)  53;  arrival;    4858_52;    -23.624329;    -46.649160

        Entries 2 and 4 will be removed because the trip 4858_73 is incomplete,
        which means that the data point with action 'arrival' is missing.

        The following metrics are currently computed in the cleaned dataset:
         - total_datapoints (int): The actual size of the dataset, each entry is a data point
         - first_move (int): The tick of the first action recorded in the simulation
         - stop_time (int): The total time or duration of the simulation given by the number of ticks
         - unique_trips (int): Total number of trips recorded based on the 'vid' <- vehicle id
         - avg_points_per_trip (float): Average of points recorded by each trip given by the total_datapoints/unique_trips
         - discarded_trips (int): Number of trips discarded by the cleaning criteria

        In order to compute the metrics the Pipeline must be given a valid Project
        to evaluate its properties and settings.

        :param project: The project object on which this Pipeline applies
    """
    def __init__(self, project):
        self.csv = project.input_csv
        self.nrows = project.nrows
        self.dest_dir = project.name
        self.summary = dict()
        self.data = None

    def run(self):
        self.data = self.load_dataset()
        self.compute_metrics(self.data)

    def save(self):
        self.save_metrics()
        #self.clip_unfinished_trips()

    def _clip_unfinished_trips(self):
        print('Removing unfinished trips')

    def _compute_metrics(self) -> Dict:
        if self.data == None: print("No metrics to compute"); return

        self.summary['total_datapoints'] = len(self.data)

        return self.summary

    def _save_metrics(self, save_to='.META'):
        """
        Save metrics in the json format inside the project directory.

        :param save_to: name of the file which the metrics will be saved
        """

        print('Saving project info to %s inside %s' % (save_to, self.dest_dir))

        save_to = self.dest_dir + '/' + save_to

        with open(save_to, 'w') as f:
            f.write(self.metrics_to_json(metrics))

    def _metrics_to_json(self):
        return json.dumps(self.metrics, indent=2)

    @staticmethod
    def load_dataset(csv, nrows=None):
        columns = ['time', 'action', 'vid', 'lat', 'lon']
        try:
            dataframe =  pd.read_csv(csv, nrows=nrows, names=columns, delimiter=";", header=None)
        except Exception as e:
            print('Could not load dataset from %s' % csv)
            dataframe =  None

        return dataframe

