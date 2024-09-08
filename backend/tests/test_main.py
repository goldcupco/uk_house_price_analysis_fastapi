from fastapi.testclient import TestClient
from app.main import app
import unittest
import matplotlib
matplotlib.use('Agg')

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_regions(self):
        response = self.client.get("/api/regions")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('regions', data)
        self.assertIsInstance(data['regions'], list)
        self.assertIn("Nationwide", data['regions'])
    
    def test_get_region_data_across_uk(self):
        response = self.client.get("/api/plots/Nationwide")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("plots", data)
        self.assertIn("average_price", data["plots"])
        self.assertIn("cumulative_change", data["plots"])

    def test_get_region_data_specific_region(self):
        response = self.client.get("/api/plots/Cambridge")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("plots", data)
        self.assertIn("average_price", data["plots"])
        self.assertIn("cumulative_change", data["plots"])
        self.assertIn("property_type", data["plots"])
        self.assertIn("property_type_change", data["plots"])

    def test_get_region_data_invalid_region(self):
        response = self.client.get("/api/plots/InvalidRegion")
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()