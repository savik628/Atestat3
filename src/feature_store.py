import pandas as pd
import os

class SimpleFeatureStore:
    def __init__(self):
        os.makedirs('features/offline', exist_ok=True)
        os.makedirs('features/online', exist_ok=True)
    
    def save_offline(self, name, features):
        features.to_parquet(f'features/offline/{name}.parquet')
    
    def load_offline(self, name):
        return pd.read_parquet(f'features/offline/{name}.parquet')
    
    def save_online(self, customer_id, features):
        features.to_json(f'features/online/{customer_id}.json')
    
    def list_features(self):
        return os.listdir('features/offline')
