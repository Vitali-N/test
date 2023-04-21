FROM python:3.9-slim

WORKDIR /app

RUN \
    apt update && \ 
    apt install -y curl


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#COPY app.py .

CMD ["python", "app.py"]