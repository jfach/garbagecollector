import os
import unittest

REPO_DIR = os.path.abspath('..')


class TestFixture(unittest.TestCase):
    """
    Fixture for unit tests
    """
    def setUp(self):
        print("Testing in: %s" % REPO_DIR)
