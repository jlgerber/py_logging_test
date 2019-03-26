"""
constants.py

All the constants in the project, in one handy location
"""
__all__ = "AD_OS AD_SHOW AD_SEQ AD_SHOT AD_FARM AD_USER AD_FORMAT".split()

AD_OS = "AD_OS"
AD_SHOW = "AD_SHOW"
AD_SEQ = "AD_SEQ"
AD_SHOT = "AD_SHOT"
AD_USER = "USER"
AD_FARM = "AD_FARM"
AD_FORMAT = \
    "%(name)-12s | %(ad_level)-8s | %(ad_os)-5s | %(levelname)-8s | %(ad_user)-3s | %(message)s"
AD_LOGLEVEL_ENVNAME = "AD_LOGLEVEL"
