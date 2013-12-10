import yaml
import os


def mkdir_p(pp):
    if os.path.isdir(pp):
        return
    if pp.startswith('~/'):
        pp = os.path.join(path.expanduser('~'), pp[2:])
    os.makedirs(pp)


class ADict(dict):

    ''' access to dict keys as object attributes

        >>> d = ADict()
        >>> d['foo'] = 'bar'
        >>> d.foo
        'bar'
        >>> d.spam = 'ham'
        >>> d['spam']
        'ham'

    source: https://github.com/rahulg/mongorm/blob/master/mongorm/utils.py
    '''

    def __init__(self, *args, **kwargs):
        super(ADict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        return self.__getitem__(key)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __delattr__(self, key):
        self.__delitem__(key)


class Config(object):

    def __init__(self, conf_file=''):
        self.conf = ADict()
        self.path = self._find_config(conf_file)
        self.load()

    def _find_config(self, conf_file=''):
        '''return fully qualified path to a config file
        if not passed directly, look in the current working dir
        or as specified by DACETS_HOME env var
        or look in $HOME/.config/dacets'''

        if os.path.isfile(conf_file):
            if os.path.splitext(conf_file)[1] == '.yml':
                return os.path.abspath(conf_file)

        cf_name = 'config.yml'
        cf_local = os.path.join(os.getcwd(), cf_name)
        cf_env = os.path.join(os.environ.get('DACETS_HOME', ''), cf_name)
        cf_home_dir = os.path.join(os.environ.get('HOME'), '.config', 'dacets')
        cf_home = os.path.join(cf_home_dir, cf_name)

        if os.path.isfile(cf_local):
            path = cf_local
        elif os.path.isfile(cf_env):
            path = cf_env
        elif os.path.isfile(cf_home):
            path = cf_home
        else:
            raise Exception('Failed to find config file')

        return os.path.abspath(path)

    def load(self):
        try:
            self.conf.update(yaml.load(open(self.path, 'r').read()))
        except Exception, e:
            print(e)

    def set(self, section, key, val):
        if self.conf.get(section, None) is None:
            # keep attr based access to 1st level (section)
            self.conf[section] = {}
        self.conf[section].update({key: value})

    def remove(self, section, name):
        try:
            self.conf[section].__delitem__(name)
        except:
            pass

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.path)
