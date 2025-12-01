import unittest
import pandas as pd
from visualizer import Visualizer

class TestVisualizer(unittest.TestCase):

    def setUp(self):
        data = {
            "Dose_µM": [0, 5, 10],
            "Viability_percent": [100, 80, 60]
        }
        self.df = pd.DataFrame(data)
        self.viz = Visualizer()

    def test_line_plot(self):
        self.viz.line_plot(self.df, "Dose_µM", "Viability_percent")

if __name__ == "__main__":
    unittest.main()
