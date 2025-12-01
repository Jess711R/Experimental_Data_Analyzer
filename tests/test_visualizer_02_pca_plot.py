import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import pandas as pd
from visualizer import Visualizer

class TestPCAPlot(unittest.TestCase):

    def test_pca_plot_runs(self):
        df = pd.DataFrame({"A": [1,2,3], "B": [4,5,6]})
        vis = Visualizer()

        try:
            vis.pca_plot(df)
        except Exception as e:
            self.fail(f"PCA plot raised {e}")