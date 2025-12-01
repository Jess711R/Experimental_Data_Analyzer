import unittest
import pandas as pd
from visualizer import Visualizer

class TestHeatmap(unittest.TestCase):

    def test_heatmap_runs(self):
        """Heatmap should run without raising exceptions."""
        df = pd.DataFrame({
            "A": [1, 2, 3, 4],
            "B": [4, 3, 2, 1],
            "C": [10, 20, 30, 40]
        })

        viz = Visualizer()

        try:
            viz.heatmap(df)   # should not raise any exception
            ran_successfully = True
        except Exception:
            ran_successfully = False

        self.assertTrue(ran_successfully)
