from .dictmerge import merge
from .constants import AD_FARM

def config(predicate_fn, dct, update_dct):
    """
    Given a callable predicate,return dct merged with update_dct if the predicate
    returns True, else return dct
    """
    if predicate_fn() is True:
        return merge(dct, update_dct)
    return dct


def on_farm_predicate():
    import os
    farm = os.environ.get(AD_FARM, None)
    if farm == "" or farm is None:
        print "on farm: False"
        return False
    print "on farm: True"
    return True