"""
More or less a direct "homage" to stackoverflow code, with the
exception of not merging lists, and raising a KeyError instead of an Exception.
"""
def merge(dict_a, dict_b, path=None, update=True):
    """
    Given two dicts, dict_a and dict_b, merge dict_b into dict_a.
    code from:
    "http://stackoverflow.com/questions/7204805/python-dictionaries-of-dictionaries-merge"

    :param dict_a: The dictionary we wish to update
    :parm dict_b: The dictionary we wish to update `dict_a` with
    :returns: dict_a
    :raises: KeyError
    """
    if path is None:
        path = []
    for key in dict_b:
        if key in dict_a:
            if isinstance(dict_a[key], dict) and isinstance(dict_b[key], dict):
                merge(dict_a[key], dict_b[key], path + [str(key)])
            elif dict_a[key] == dict_b[key]:
                pass # same leaf value
            elif isinstance(dict_a[key], list) and isinstance(dict_b[key], list):
                # we replace lists instead of merging their contents.
                #for idx, val in enumerate(dict_b[key]):
                #    dict_a[key][idx] = merge(dict_a[key][idx], dict_b[key][idx], \
                # path + [str(key), str(idx)], update=update)
                dict_a[key] = dict_b[key]
            elif update:
                dict_a[key] = dict_b[key]
            else:
                raise KeyError('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            dict_a[key] = dict_b[key]
    return dict_a
