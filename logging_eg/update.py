"""
update.py

update.config is a function which allows us to conditionally
update a dictionary. Why would we want to use this? To change
logging levels when on the farm, for instance.
"""

from .dictmerge import merge

def config(predicate_fn, dct, update_dct):
    """
    Given a callable predicate,return dct merged with update_dct if the predicate
    returns True, else return dct
    """
    if predicate_fn() is True:
        return merge(dct, update_dct)
    return dct
