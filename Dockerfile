# FROM node:22-alpine AS builder
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . .
# RUN npm run build

FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# COPY --from=builder /app/static/css/output.css /app/static/css/output.css
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "sukanews.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=3", "--timeout=30"]