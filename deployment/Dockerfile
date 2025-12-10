FROM python:3.9-slim

WORKDIR /app

# Копируем зависимости
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY api/ ./api/
COPY src/models/xgb_final_model.pkl ./src/models/
COPY src/feature_store.py ./src/

# Создаём недостающие папки
RUN mkdir -p features/offline features/online

# Запускаем сервер
EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
