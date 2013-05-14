class AttrDict(dict):
    """ access to dict keys as object attributes

        >>> d = AttrDict()
        >>> d['foo'] = 'bar'
        >>> d.foo
        'bar'
        >>> d.spam = 'ham'
        >>> d['spam']
        'ham'

    source: https://github.com/rahulg/mongorm/blob/master/mongorm/utils.py
    """

    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        return self.__getitem__(key)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __delattr__(self, key):
        del self[key]
