import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from data_loader import DataLoader

class TestInvalidFile(unittest.TestCase):

    def test_invalid_file(self):
        loader = DataLoader()
        with self.assertRaises(FileNotFoundError):
            loader.load("sample_data/does_not_exist.csv")