FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN \
    pip install --no-cache-dir -r requirements.txt
#    pip3 install prometheus-client

#COPY app.py .

CMD ["python", "app.py"]