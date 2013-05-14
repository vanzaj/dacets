import os
import unittest
import dacets

here = os.path.dirname(__file__)

class TestConfig(unittest.TestCase):

    def test_config_yml(self):
        cf_path = os.path.join(here, 'mocks', 'config.yml')
        c = dacets.config.Config(cf_path)
        self.assertEqual(c.path, cf_path)
        self.assertTrue('Feynman' in c.conf.user['name'])

    def test_config_ini(self):
        cf_path = os.path.join(here, 'mocks', 'config.ini')
        c = dacets.config.Config(cf_path)
        self.assertEqual(c.path, cf_path)
        self.assertTrue('Feynman' in c.conf.user['name'])
