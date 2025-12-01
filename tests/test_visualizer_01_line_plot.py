import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import pandas as pd
from visualizer import Visualizer

class TestLinePlot(unittest.TestCase):

    def test_line_plot_runs(self):
        df = pd.DataFrame({"x": [1,2,3], "y": [4,5,6]})
        vis = Visualizer()

        try:
            vis.line_plot(df, "x", "y")
        except Exception as e:
            self.fail(f"line_plot raised {e}")