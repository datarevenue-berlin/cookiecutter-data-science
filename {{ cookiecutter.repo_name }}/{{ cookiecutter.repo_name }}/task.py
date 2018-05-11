import luigi
import datetime as dt
from drtools.utils.task import DockerTask

class LivePredict(DockerTask):

    date = luigi.DateParameter(default=dt.date.today())

    def requires(self):
        pass

    def output(self):
        pass

    def run(self):
        pass