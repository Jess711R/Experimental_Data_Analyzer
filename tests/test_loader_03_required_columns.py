import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from data_loader import DataLoader

class TestRequiredColumns(unittest.TestCase):

    def test_required_columns_present(self):
        loader = DataLoader()
        df = loader.load("sample_data/MCF7_MTT_small.csv")
        self.assertIn("SampleID", df.columns)