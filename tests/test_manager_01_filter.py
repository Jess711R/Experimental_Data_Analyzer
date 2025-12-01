import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import pandas as pd
from data_manager import DataManager

class TestFilter(unittest.TestCase):

    def test_filter(self):
        df = pd.DataFrame({
            "treatment": ["Control", "DrugA", "DrugA"],
            "value": [5, 10, 20]
        })

        manager = DataManager(df)
        result = manager.filter(treatment="DrugA")
        self.assertEqual(len(result), 2)