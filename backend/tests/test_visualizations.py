import unittest
import pandas as pd
import matplotlib.pyplot as plt
from app.visualizations import (
    check_data_integrity,
    create_average_price_plot,
    create_cumulative_change_plot,
    create_property_type_plot,
    create_property_type_change_plot,
    create_all_plots
)

class TestVisualizations(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        self.data = pd.DataFrame({
            'Date': pd.date_range(start='2020-01-01', periods=12, freq='M'),
            'RegionName': ['London'] * 12,
            'AveragePrice': range(100000, 112000, 1000),
            'DetachedPrice': range(150000, 162000, 1000),
            'SemiDetachedPrice': range(120000, 132000, 1000),
            'TerracedPrice': range(90000, 102000, 1000),
            'FlatPrice': range(80000, 92000, 1000)
        })

    def test_check_data_integrity(self):
        check_data_integrity(self.data)  # Should not raise an exception

        # Test with missing column
        with self.assertRaises(ValueError):
            bad_data = self.data.drop('AveragePrice', axis=1)
            check_data_integrity(bad_data)

    def test_create_average_price_plot(self):
        fig = create_average_price_plot(self.data, 'London')
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_create_cumulative_change_plot(self):
        fig = create_cumulative_change_plot(self.data, 'London')
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_create_property_type_plot(self):
        fig = create_property_type_plot(self.data, 'London')
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_create_property_type_change_plot(self):
        fig = create_property_type_change_plot(self.data, 'London')
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_create_all_plots(self):
        plots = create_all_plots(self.data, 'London')
        self.assertIsInstance(plots, dict)
        self.assertEqual(len(plots), 4)  # Expecting 4 plots for a single region
        for fig in plots.values():
            self.assertIsInstance(fig, plt.Figure)
            plt.close(fig)

if __name__ == '__main__':
    unittest.main()