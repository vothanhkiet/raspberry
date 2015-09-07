import psutil
import logging

__author__ = 'archer'


class SystemInfo(object):

    def __init__(self):
        self.log = logging.getLogger(SystemInfo.__name__)
        self.cpu_count = psutil.cpu_count()

    def get_cpu_percent(self):
        cpu = str(psutil.cpu_percent() / self.cpu_count)
        if self.log.isEnabledFor(logging.INFO):
            self.log.info(cpu)
        return cpu
