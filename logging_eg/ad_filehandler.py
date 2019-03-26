"""
AdFileHandler implements custom logic to identify level at runtime
"""

import logging
import os
from .fauxlevelspec import LevelSpec

LOCATION = os.path.dirname(os.path.dirname(__file__))

class AdFileHandler(logging.FileHandler):
    """
    AdFileHandler has the same init signature as loggingFileHandler, but
    it identifies file logging location based on the level set
    """
    def __init__(self, filename, mode='a', encoding=None, delay=0):
        self.__filename = filename
        super(AdFileHandler, self).__init__(filename, mode, encoding, delay)

    @property
    def baseFilename(self):
        """
        the superclass uses baseFilename to access file logger location.
        """
        level = LevelSpec.from_env()
        if level.is_valid():
            logdir = os.path.join(LOCATION,"logoutput", "ad", "shows", level.path(), "LOGS")
            if not os.path.exists(logdir):
                os.makedirs(logdir)
            rval = os.path.join(logdir, self.__filename)
            return rval
        else:
            return os.path.join(LOCATION, "logoutput","ad","dept","logs", self.__filename)

    @baseFilename.setter
    def baseFilename(self, value):
        pass