from tempfile import mktemp

import luigi
import logging

logger = logging.getLogger('luigi-interface')

class MakeForecast(luigi.Task):

    def requires(self):
        return None

    def run(self):
        logger.info("Project setup successful correctly")
        with self.output().open('w') as f:
            f.write("YEY")

    def output(self):
        return luigi.LocalTarget(mktemp())