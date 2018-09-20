import json
import pandas as pd

class SummaryStats():
    def __init__(self, project):
        self.csv = project.input_csv
        self.nrows = project.nrows
        self.dest_dir = project.name
        self.summary = dict()

    def run(self):
        self.data = self.load_dataset()
        self.collect_metrics()
        self.save_metrics()
        #self.clip_unfinished_trips()

    def clip_unfinished_trips(self):
        print("Removing unfinished trips")

    def load_dataset(self):
        columns = ['time', 'action', 'vid', 'lat', 'lon']
        return pd.read_csv(self.csv, nrows=self.nrows, names=columns, delimiter=";", header=None)

    def collect_metrics(self):
        self.summary['total_datapoints'] = len(data)

    def save_metrics(self, save_to='.META'):
        print("Saving project info to %s inside %s" % (save_to, self.dest_dir))

        save_to = self.dest_dir + '/' + save_to

        with open(save_to, 'w') as f:
            f.write(self.metrics_to_json(metrics))

    def metrics_to_json(self):
        return json.dumps(self.metrics, indent=2)
