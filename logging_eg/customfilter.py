"""
customfilter.py

Implementation of filter which decorates logRecord with additional
information from the environment.
"""
import logging
import os

from .constants import *

class AdFilter(logging.Filter):
    """
    Custom filter test for a ficticious VFX company called Analog Domain, or AD
    """
    def filter(self, record):
        record.ad_level = self._get_level()
        record.ad_user = os.environ.get(AD_USER)
        record.ad_os = os.environ.get(AD_OS)
        return super(AdFilter, self).filter(record)

    def _get_level(self):
        return ".".join(filter(None,[os.environ.get(x) for x in ("AD_SHOW", "AD_SEQ", "AD_SHOT")]))


