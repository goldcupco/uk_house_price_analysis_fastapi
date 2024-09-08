import unittest
from app.data_loader import load_and_preprocess_data

class TestDataLoader(unittest.TestCase):
    def test_load_and_preprocess_data(self):
        df = load_and_preprocess_data()
        self.assertIsNotNone(df)
        self.assertGreater(len(df), 0)
        # Add more assertions as needed to test the data

if __name__ == '__main__':
    unittest.main()
    
    