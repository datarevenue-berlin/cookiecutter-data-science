import luigi
import datetime as dt
from drtools.utils.task import DockerTask
from .structure import PATH

class Example(DockerTask):

    @property
    def image(self):
        return 'test-template'

    @property
    def command(self):
        return ['python', '-m', 'project_name.data.dataset']

    @property
    def name(self):
        return 'test-template-container'

    def requires(self):
        return ClientUpload()

    def output(self):
        return luigi.LocalTarget(PATH['CS_OUT'])


class ClientUpload(luigi.ExternalTask):

    def output(self):
        return luigi.LocalTarget(PATH['CS_IN'])