# FROM python:3.10-slim
# WORKDIR /app
# RUN apt-get update && apt-get install -y \
#     postgresql-client \
#     libpq-dev \
#     build-essential
# RUN pip install gunicorn==20.1.0 
# COPY requirements.txt .
# RUN pip install --upgrade pip
# COPY requirements.txt ./
# RUN pip install -r requirements.txt --no-cache-dir
# COPY . ./
# CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]
FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir
COPY . ./
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]
