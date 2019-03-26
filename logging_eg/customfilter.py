"""
customfilter.py

Implementation of filter which decorates logRecord with additional
information from the environment.
"""
import logging
import os

from .constants import (AD_USER, AD_OS)
from .fauxlevelspec import LevelSpec

class AdFilter(logging.Filter):
    """
    Custom filter test for a ficticious VFX company called Analog Domain, or AD
    """
    def filter(self, record):
        """
        Add custom content to the record and then call the superclass's
        filter method, returning the results.
        """
        record.ad_level = self._get_level()
        record.ad_user = os.environ.get(AD_USER)
        record.ad_os = os.environ.get(AD_OS)
        return super(AdFilter, self).filter(record)

    @staticmethod
    def _get_level():
        """
        We return FACILITY if we are not in a show.
        """
        level = LevelSpec.from_env()
        if level.is_valid():
            return str(level)
        else:
            return "FACILITY"


