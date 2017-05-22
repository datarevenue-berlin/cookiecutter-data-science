import luigi
import datetime as dt


class LivePredict(luigi.Task):

    date = luigi.DateParameter(default=dt.date.today())

    def requires(self):
        pass

    def output(self):
        pass

    def run(self):
        pass