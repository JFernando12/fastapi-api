FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY alembic.ini .
COPY alembic/ ./alembic/
COPY src/ ./src/

EXPOSE 3000

CMD ["sh", "-c", "alembic upgrade head && python -m src.main"]