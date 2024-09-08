import unittest
import pandas as pd
import matplotlib.pyplot as plt
from app.visualizations import create_average_price_plot, create_cumulative_change_plot, create_property_type_plot, create_property_type_change_plot

class TestVisualizations(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        self.test_data = pd.DataFrame({
            'Date': pd.date_range(start='2020-01-01', end='2020-12-31', freq='ME'),
            'AveragePrice': range(100000, 112000, 1000),
            'DetachedPrice': range(150000, 162000, 1000),
            'SemiDetachedPrice': range(120000, 132000, 1000),
            'TerracedPrice': range(90000, 102000, 1000),
            'FlatPrice': range(80000, 92000, 1000)
        })

    def test_create_average_price_plot(self):
        fig, data = create_average_price_plot(self.test_data, "Test Region")
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

    def test_create_cumulative_change_plot(self):
        fig, data = create_cumulative_change_plot(self.test_data, "Test Region")
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

    def test_create_property_type_plot(self):
        fig, data = create_property_type_plot(self.test_data, "Test Region")
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

    def test_create_property_type_change_plot(self):
        fig, data = create_property_type_change_plot(self.test_data, "Test Region")
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

if __name__ == '__main__':
    unittest.main()