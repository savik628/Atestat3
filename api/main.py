from fastapi import FastAPI
import pandas as pd
import joblib
import numpy as np

app = FastAPI()

# Загружаем модель и информацию о фичах
model = joblib.load('src/models/xgb_final_model.pkl')

# Все признаки которые ожидает модель (20 штук)
EXPECTED_FEATURES = [
    'CustomerID', 'Tenure', 'PreferredLoginDevice', 'CityTier', 
    'WarehouseToHome', 'PreferredPaymentMode', 'Gender', 
    'HourSpendOnApp', 'NumberOfDeviceRegistered', 'PreferedOrderCat', 
    'SatisfactionScore', 'MaritalStatus', 'NumberOfAddress', 
    'Complain', 'OrderAmountHikeFromlastYear', 'CouponUsed', 
    'OrderCount', 'DaySinceLastOrder', 'CashbackAmount', 'CustomerLoyalty'
]

# Значения по умолчанию для отсутствующих признаков
DEFAULT_VALUES = {
    'CustomerID': 999999,
    'PreferredLoginDevice': 'Mobile Phone',
    'CityTier': 2,
    'WarehouseToHome': 10.0,
    'PreferredPaymentMode': 'Debit Card',
    'Gender': 'Male',
    'HourSpendOnApp': 3.0,
    'NumberOfDeviceRegistered': 3,
    'PreferedOrderCat': 'Laptop & Accessory',
    'SatisfactionScore': 3,
    'MaritalStatus': 'Single',
    'NumberOfAddress': 5,
    'OrderAmountHikeFromlastYear': 15.0,
    'CouponUsed': 1.0,
    'DaySinceLastOrder': 5.0,
    'CustomerLoyalty': 30.0  # Tenure * OrderCount
}

@app.post("/predict")
def predict(data: dict):
    """Предсказание оттока"""
    # Начинаем со значений по умолчанию
    features = DEFAULT_VALUES.copy()
    
    # Обновляем переданными значениями
    features.update(data)
    
    # Создаём DataFrame в правильном порядке
    df = pd.DataFrame([features])[EXPECTED_FEATURES]
    
    # Кодируем категориальные (простейший способ)
    for col in ['PreferredLoginDevice', 'PreferredPaymentMode', 
                'Gender', 'PreferedOrderCat', 'MaritalStatus']:
        df[col] = df[col].astype('category').cat.codes
    
    # Предсказание
    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])
    
    return {
        "churn": prediction,
        "probability": probability,
        "features_used": len(EXPECTED_FEATURES)
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/features")
def features():
    return {"expected_features": EXPECTED_FEATURES}
