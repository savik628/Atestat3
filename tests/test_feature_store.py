import unittest
import pandas as pd
import sys
sys.path.append('src')
from feature_store import SimpleFeatureStore

class TestFeatureStore(unittest.TestCase):
    def setUp(self):
        self.fs = SimpleFeatureStore()
        self.df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    
    def test_save_load(self):
        self.fs.save_offline('test', self.df)
        loaded = self.fs.load_offline('test')
        self.assertEqual(len(loaded), 2)
    
    def tearDown(self):
        import shutil
        shutil.rmtree('features', ignore_errors=True)

if __name__ == '__main__':
    unittest.main()
