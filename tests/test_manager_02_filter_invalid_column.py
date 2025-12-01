import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import pandas as pd
from data_manager import DataManager

class TestFilterInvalidColumn(unittest.TestCase):

    def test_filter_invalid_column(self):
        df = pd.DataFrame({"a": [1], "b": [2]})
        manager = DataManager(df)

        with self.assertRaises(KeyError):
            manager.filter(fake="value")