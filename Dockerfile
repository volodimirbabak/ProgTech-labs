FROM python:3.11-slim

WORKDIR /app

# копіюємо код
COPY . .

# запуск тестів під час білду
RUN python -m unittest discover

CMD ["python"]
