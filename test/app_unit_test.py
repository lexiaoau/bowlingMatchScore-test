#!/usr/bin/python3
from unittest.mock import patch
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../app")

from App import App

class TestAppClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = App()             # app instance to run test on

    def test_app_simpleRoll(self):        

        self.app.rollAll( [] )
        self.assertEqual(0, self.app.score() )

        oneRoll = 9
        self.app.rollAll( [oneRoll] )
        self.assertEqual(oneRoll, self.app.score() )





