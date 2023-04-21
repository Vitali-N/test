from flask import Flask
from flask_healthz import healthz, HealthError
#from prometheus_client import Counter, Gauge, start_http_server
#import time

#REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')
#EXCEPTIONS = Counter('http_exceptions_total', 'Total HTTP Exceptions')
#LATENCY = Gauge('http_request_latency_seconds', 'HTTP Request Latency')

app = Flask(__name__)
app.register_blueprint(healthz, url_prefix="/healthz")

@app.route('/')
def hello():
#    REQUESTS.inc()
#    start_time = time.time()
    try:
        return 'Hello, World!'
#    except Exception as e:
#        EXCEPTIONS.inc()
#        raise e
#    finally:
#        LATENCY.observe(time.time() - start_time)


# Health Check
def liveness():
    try:
        return 'liveness - OK'
    except Exception:
        raise HealthError("Can't connect to the file")

# Readiness Check
def readiness():
    try:
        return 'readiness - OK'
    except Exception:
        raise HealthError("Can't connect to the file")


app.config.update(
    HEALTHZ = {
        "live": "app.liveness",
        "ready": "app.readiness",
    }
)

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
    while True:
       pass
