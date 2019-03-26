"""
predicates.py

Exxample predicate functions. A predicate is a callable which
returns True or False.
"""
from .constants import AD_FARM

def on_farm():
    """
    Test to see if we are on our fictitous farm. Oh, an alliteration. I like those.
    fictitous farm, fictitous farm, fictitous farm...
    """
    import os
    farm = os.environ.get(AD_FARM, None)
    if farm == "" or farm is None:
        return False
    return True

def true():
    """
    always return true
    """
    return True

def false():
    """
    always return false
    """
    return False

def boolean(value):
    """
    given a value that should be a boolean, return a function that
    returns the value when called.
    """
    def _boolean():
        return value
    return _boolean
