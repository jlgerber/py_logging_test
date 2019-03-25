"""
More or less a direct "homage" to stackoverflow code, with the
exception of not merging lists, and raising a KeyError instead of an Exception.
"""
def merge(a, b, path=None, update=True):
    """
    Given two dicts, a and b, merge b into a.
    code from: "http://stackoverflow.com/questions/7204805/python-dictionaries-of-dictionaries-merge"

    :param a: The dictionary we wish to update
    :parm b: The dictionary we wish to update `a` with
    :returns: a
    :raises: KeyError
    """
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            elif isinstance(a[key], list) and isinstance(b[key], list):
                # we replace lists instead of merging their contents.
                #for idx, val in enumerate(b[key]):
                #    a[key][idx] = merge(a[key][idx], b[key][idx], path + [str(key), str(idx)], update=update)
                a[key] = b[key]
            elif update:
                a[key] = b[key]
            else:
                raise KeyError('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a