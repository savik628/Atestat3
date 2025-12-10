
-- RAW LAYER
CREATE TABLE raw_customers (
    customer_id INT,
    churn INT,
    tenure FLOAT,
    preferred_login_device TEXT,
    city_tier INT,
    warehouse_to_home FLOAT,
    preferred_payment_mode TEXT,
    gender TEXT,
    hour_spend_on_app FLOAT,
    number_of_device_registered INT,
    prefered_order_cat TEXT,
    satisfaction_score INT,
    marital_status TEXT,
    number_of_address INT,
    complain INT,
    order_amount_hike_from_last_year FLOAT,
    coupon_used FLOAT,
    order_count FLOAT,
    day_since_last_order FLOAT,
    cashback_amount FLOAT,
    load_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CLEANED LAYER
CREATE TABLE cleaned_customers (
    customer_id INT PRIMARY KEY,
    churn INT,
    tenure FLOAT NOT NULL DEFAULT 0,
    preferred_login_device TEXT,
    city_tier INT,
    warehouse_to_home FLOAT NOT NULL DEFAULT 0,
    preferred_payment_mode TEXT,
    gender TEXT,
    hour_spend_on_app FLOAT NOT NULL DEFAULT 0,
    number_of_device_registered INT,
    prefered_order_cat TEXT,
    satisfaction_score INT,
    marital_status TEXT,
    number_of_address INT,
    complain INT,
    order_amount_hike_from_last_year FLOAT NOT NULL DEFAULT 0,
    coupon_used FLOAT NOT NULL DEFAULT 0,
    order_count FLOAT NOT NULL DEFAULT 0,
    day_since_last_order FLOAT NOT NULL DEFAULT 0,
    cashback_amount FLOAT,
    customer_loyalty FLOAT,
    clean_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- FEATURES LAYER
CREATE TABLE features_customers (
    customer_id INT PRIMARY KEY,
    churn INT,
    tenure_scaled FLOAT,
    city_tier_encoded INT,
    warehouse_to_home_scaled FLOAT,
    gender_encoded INT,
    hour_spend_on_app_scaled FLOAT,
    number_of_device_registered INT,
    satisfaction_score INT,
    number_of_address INT,
    complain INT,
    order_amount_hike_from_last_year_scaled FLOAT,
    coupon_used_scaled FLOAT,
    order_count_scaled FLOAT,
    day_since_last_order_scaled FLOAT,
    cashback_amount_scaled FLOAT,
    customer_loyalty_scaled FLOAT,
    feature_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
