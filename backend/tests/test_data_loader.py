import unittest
from app.data_loader import load_and_preprocess_data

class TestDataLoader(unittest.TestCase):
    def test_load_and_preprocess_data(self):
        df = load_and_preprocess_data()
        self.assertIsNotNone(df)
        self.assertIn('Date', df.columns)
        self.assertIn('Index', df.columns)
        # Add more assertions as needed

if __name__ == '__main__':
    unittest.main()