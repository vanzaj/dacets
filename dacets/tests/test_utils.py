import os
import unittest

from dacets.utils import *

here = os.path.dirname(__file__)


def test_mkdir_p():
    os.chdir(here)
    p1 = 'test_mkdir_p'
    assert os.path.isdir(p1) is False
    p2 = os.path.join(p1, 'some', 'junk')
    mkdir_p(p2)
    assert os.path.isdir(p2) is True
    os.removedirs(p2)
    assert os.path.isdir(p1) is False


class TestADict(unittest.TestCase):

    def test_ADict_set_get(self):
        d = ADict()
        d.foo = 'bar'
        self.assertEqual(d['foo'], 'bar')
        self.assertEqual(d.foo, 'bar')

    def test_ADict_from_dict(self):
        d = dict(a=1, b=2, c='three')
        ad = ADict(d)
        self.assertEqual(ad.a, d['a'])
        self.assertEqual(ad.b, d['b'])
        self.assertEqual(ad.c, d['c'])

    def test_ADict_del(self):
        d = ADict({'a': 1, 'b': 2})
        del(d.a)
        self.assertFalse('a' in d.keys())


class TestConfig(unittest.TestCase):

    def test_config_yml(self):
        cf = os.path.join(here, 'mocks', 'config.yml')
        c = Config(cf)
        self.assertEqual(c.path, cf)
        self.assertTrue('Feynman' in c.conf.user['name'])
