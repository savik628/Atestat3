
-- 1. Анализ пропусков
SELECT 
    COUNT(*) - COUNT(tenure) as missing_tenure,
    COUNT(*) - COUNT(warehouse_to_home) as missing_warehouse,
    COUNT(*) - COUNT(hour_spend_on_app) as missing_hours
FROM raw_customers;

-- 2. Распределение Churn
SELECT 
    churn,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentage
FROM cleaned_customers
GROUP BY churn;

-- 3. Топ-3 признака по корреляции с Churn (пример)
SELECT 
    ''tenure'' as feature,
    CORR(tenure, churn) as correlation
FROM cleaned_customers
UNION ALL
SELECT 
    ''cashback_amount'',
    CORR(cashback_amount, churn)
FROM cleaned_customers
UNION ALL
SELECT 
    ''complain'',
    CORR(complain, churn)
FROM cleaned_customers
ORDER BY ABS(correlation) DESC;

-- 4. Выборка для обучения (последние 80%)
SELECT * FROM features_customers 
WHERE customer_id IN (
    SELECT customer_id FROM cleaned_customers 
    ORDER BY customer_id 
    LIMIT (SELECT COUNT(*) * 0.8 FROM cleaned_customers)
);

-- 5. Статистика по слоям
SELECT 
    ''raw'' as layer, 
    COUNT(*) as rows, 
    COUNT(DISTINCT customer_id) as unique_ids
FROM raw_customers
UNION ALL
SELECT 
    ''cleaned'', COUNT(*), COUNT(DISTINCT customer_id)
FROM cleaned_customers
UNION ALL
SELECT 
    ''features'', COUNT(*), COUNT(DISTINCT customer_id)
FROM features_customers;
