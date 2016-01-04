import os
import unittest

UNIT_DIR = os.path.abspath(os.path.dirname(__file__))
REPO_DIR = os.path.join(UNIT_DIR, '..')


class TestFixture(unittest.TestCase):
    """
    Fixture for unit tests
    """
    def setUp(self):
        print("Testing in: %s" % REPO_DIR)
