import os
from os import path


def mkdir_p(pp):
    if path.isdir(pp):
        return
    if pp.startswith('~/'):
        pp = path.join(path.expanduser('~'), pp[2:])
    os.makedirs(pp)


class ADict(dict):
    """ access to dict keys as object attributes

        >>> d = ADict()
        >>> d['foo'] = 'bar'
        >>> d.foo
        'bar'
        >>> d.spam = 'ham'
        >>> d['spam']
        'ham'

    source: https://github.com/rahulg/mongorm/blob/master/mongorm/utils.py
    """

    def __init__(self, *args, **kwargs):
        super(ADict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        return self.__getitem__(key)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __delattr__(self, key):
        self.__delitem__(key)

