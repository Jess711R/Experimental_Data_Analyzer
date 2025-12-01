import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import pandas as pd
from data_manager import DataManager

class TestStats(unittest.TestCase):

    def test_stats(self):
        df = pd.DataFrame({"num": [10, 20, 30]})
        manager = DataManager(df)
        stats = manager.stats("num")

        self.assertEqual(stats["min"], 10)
        self.assertEqual(stats["max"], 30)
        self.assertAlmostEqual(stats["mean"], 20)