"""
update a logging dict based on settings from the environment. IP. Not used
"""
from os import environ

from .constants import AD_LOGLEVEL_ENVNAME
from .dictmerge import merge
def update_config(config_dct, update_config, handlers=("adconsole", "console")):
    """
    update_config(config_dct: dict, update_config: dict, handlers: list) -> dict
    """
    raise NotImplementedError("not implemented yet")


def update_from_env(config_dict, handlers=("adconsole", "console")):
    """
    update_from_env(config_dct: dict, handlers: list) -> dict

    """
    loglevel = environ.get(AD_LOGLEVEL_ENVNAME)
    if loglevel is None:
        return config_dict

    # split by comma
    for loglevel in loglevel.split(","):
        pieces = loglevel.split("=")
        if len(pieces) > 1:
            # logger = level
            pass
        else:
            # level
            pass

    raise NotImplementedError("not implemented yet")