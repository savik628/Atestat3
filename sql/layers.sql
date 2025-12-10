
-- 1. Заполнение RAW слоя (пример из CSV)
-- COPY raw_customers FROM ''/path/to/ecommerce_churn.csv'' DELIMITER '';'' CSV HEADER;

-- 2. Заполнение CLEANED слоя (очистка данных)
INSERT INTO cleaned_customers 
SELECT 
    customer_id,
    churn,
    COALESCE(tenure, 0) AS tenure,
    preferred_login_device,
    city_tier,
    COALESCE(warehouse_to_home, 0) AS warehouse_to_home,
    preferred_payment_mode,
    gender,
    COALESCE(hour_spend_on_app, 0) AS hour_spend_on_app,
    number_of_device_registered,
    prefered_order_cat,
    satisfaction_score,
    marital_status,
    number_of_address,
    complain,
    COALESCE(order_amount_hike_from_last_year, 0) AS order_amount_hike_from_last_year,
    COALESCE(coupon_used, 0) AS coupon_used,
    COALESCE(order_count, 0) AS order_count,
    COALESCE(day_since_last_order, 0) AS day_since_last_order,
    cashback_amount,
    COALESCE(tenure, 0) * COALESCE(order_count, 0) AS customer_loyalty,
    CURRENT_TIMESTAMP
FROM raw_customers;

-- 3. Заполнение FEATURES слоя (масштабирование)
INSERT INTO features_customers 
SELECT 
    customer_id,
    churn,
    (tenure - AVG(tenure) OVER()) / NULLIF(STDDEV(tenure) OVER(), 0) AS tenure_scaled,
    city_tier AS city_tier_encoded,
    (warehouse_to_home - AVG(warehouse_to_home) OVER()) / NULLIF(STDDEV(warehouse_to_home) OVER(), 0) AS warehouse_to_home_scaled,
    CASE gender WHEN ''Male'' THEN 1 ELSE 0 END AS gender_encoded,
    (hour_spend_on_app - AVG(hour_spend_on_app) OVER()) / NULLIF(STDDEV(hour_spend_on_app) OVER(), 0) AS hour_spend_on_app_scaled,
    number_of_device_registered,
    satisfaction_score,
    number_of_address,
    complain,
    (order_amount_hike_from_last_year - AVG(order_amount_hike_from_last_year) OVER()) / NULLIF(STDDEV(order_amount_hike_from_last_year) OVER(), 0) AS order_amount_hike_from_last_year_scaled,
    (coupon_used - AVG(coupon_used) OVER()) / NULLIF(STDDEV(coupon_used) OVER(), 0) AS coupon_used_scaled,
    (order_count - AVG(order_count) OVER()) / NULLIF(STDDEV(order_count) OVER(), 0) AS order_count_scaled,
    (day_since_last_order - AVG(day_since_last_order) OVER()) / NULLIF(STDDEV(day_since_last_order) OVER(), 0) AS day_since_last_order_scaled,
    (cashback_amount - AVG(cashback_amount) OVER()) / NULLIF(STDDEV(cashback_amount) OVER(), 0) AS cashback_amount_scaled,
    (customer_loyalty - AVG(customer_loyalty) OVER()) / NULLIF(STDDEV(customer_loyalty) OVER(), 0) AS customer_loyalty_scaled,
    CURRENT_TIMESTAMP
FROM cleaned_customers;
