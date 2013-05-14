import os
import yaml
from ConfigParser import SafeConfigParser
from .utils import AttrDict


def _find_config(cf_path=''):
    """return fully qualified path to a config file
    if not passed directly, look in the current working dir
    or as specified by DACETS_HOME env var
    or look in $HOME/.config"""
    if os.path.isfile(cf_path):
        if os.path.splitext(cf_path)[1] in ['.yml', '.ini']:
            return cf_path

    local_yml = 'config.yml'
    local_ini = 'config.ini'
    env_yml = os.path.join(os.environ.get('DACETS_HOME', ''), local_yml)
    env_ini = os.path.join(os.environ.get('DACETS_HOME', ''), local_ini)
    home_conf = os.path.join(os.environ.get('HOME'), '.config', 'dacets')
    home_yml = os.path.join(home_conf, local_yml)
    home_ini = os.path.join(home_conf, local_ini)
    if os.path.isfile(local_yml): 
        path = os.path.abspath(local_yml)
    elif os.path.isfile(local_ini):
        path = os.path.abspath(local_ini)
    elif os.path.isfile(env_yml):
        path = env_yml
    elif os.path.isfile(env_ini):
        path = env_ini
    elif os.path.isfile(home_yml):
        path = home_yml
    elif os.path.isfile(home_ini):
        path = home_ini
    else:
        path = ''
    return path


class Config(object):

    def __init__(self, cf_path=''):
        self.path = _find_config(cf_path)
        self.format = os.path.splitext(self.path)[1][1:]
        self.conf = AttrDict()
        self.load()

    def load(self):
        if self.format == 'yml':
            self.conf.update(yaml.load(open(self.path, 'r').read()))
        else:
            self._load_ini()

    def _load_ini(self):
        try:
            parser = SafeConfigParser()
            parser.read(self.path)
            self.conf = AttrDict()
            for sect in parser.sections():
                self.conf[sect] = {}
                for name, val in parser.items(sect):
                    self.conf[sect][name] = val
        except Exception as e:
            # TODO: change to logger
            print(e)

    def set(self, section, key, val):
        if not self.conf.get(section, None):
            self.conf[section] = {}
        self.conf[section].update({key: value})

    def remove(self, section, name):
        try:
            self.conf[section].__delitem__(name)
        except:
            pass

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.path)

