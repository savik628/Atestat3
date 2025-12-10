import unittest
from fastapi.testclient import TestClient
import sys
sys.path.append('api')
from main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
    
    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
    
    def test_features(self):
        response = self.client.get("/features")
        self.assertEqual(response.status_code, 200)
        self.assertIn("expected_features", response.json())
    
    def test_predict_minimal(self):
        """Тест с минимальными данными"""
        data = {
            "Tenure": 12,
            "CashbackAmount": 150.0,
            "OrderCount": 10,
            "Complain": 0
        }
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn("churn", result)
        self.assertIn("probability", result)
        self.assertIn("features_used", result)
    
    def test_predict_full(self):
        """Тест с полными данными"""
        data = {
            "CustomerID": 50001,
            "Tenure": 4.0,
            "PreferredLoginDevice": "Mobile Phone",
            "CityTier": 3,
            "WarehouseToHome": 6.0,
            "PreferredPaymentMode": "Debit Card",
            "Gender": "Female",
            "HourSpendOnApp": 3.0,
            "NumberOfDeviceRegistered": 3,
            "PreferedOrderCat": "Laptop & Accessory",
            "SatisfactionScore": 2,
            "MaritalStatus": "Single",
            "NumberOfAddress": 9,
            "Complain": 1,
            "OrderAmountHikeFromlastYear": 11.0,
            "CouponUsed": 1.0,
            "OrderCount": 1.0,
            "DaySinceLastOrder": 5.0,
            "CashbackAmount": 159.93
        }
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn("churn", result)
        self.assertIn("probability", result)
        self.assertEqual(result["features_used"], 20)

if __name__ == '__main__':
    unittest.main()
