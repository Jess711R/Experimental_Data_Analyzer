import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import pandas as pd
from data_loader import DataLoader

class TestLoadCSV(unittest.TestCase):

    def test_load_csv(self):
        loader = DataLoader()
        df = loader.load("sample_data/MCF7_MTT_small.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)