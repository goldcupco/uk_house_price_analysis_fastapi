import unittest
import matplotlib.pyplot as plt
from app.data_loader import load_and_preprocess_data
from app.visualizations import create_hpi_trend_plot, create_regional_comparison_plot, create_year_on_year_change_plot

class TestVisualizations(unittest.TestCase):
    def setUp(self):
        self.df = load_and_preprocess_data()

    def test_create_hpi_trend_plot(self):
        plot = create_hpi_trend_plot(self.df)
        self.assertIsInstance(plot, plt.Figure)

    def test_create_regional_comparison_plot(self):
        plot = create_regional_comparison_plot(self.df)
        self.assertIsInstance(plot, plt.Figure)

    def test_create_year_on_year_change_plot(self):
        plot = create_year_on_year_change_plot(self.df)
        self.assertIsInstance(plot, plt.Figure)

if __name__ == '__main__':
    unittest.main()