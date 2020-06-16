# -*- coding: utf-8 -*-

import unittest
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class TestConfigExists(unittest.TestCase):

    def test_config_exists(self):
        self.assertTrue(os.path.isfile('config.toml'))


if __name__ == '__main__':
    unittest.main()