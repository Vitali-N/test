from flask import Flask
from flask_healthz import healthz
from flask_healthz import HealthError
from prometheus_client import Counter, Gauge, start_http_server
from prometheus_flask_exporter import PrometheusMetrics

#REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')
#EXCEPTIONS = Counter('http_exceptions_total', 'Total HTTP Exceptions')
#LATENCY = Gauge('http_request_latency_seconds', 'HTTP Request Latency')

app = Flask(__name__)

metrics = PrometheusMetrics(app)
app.register_blueprint(healthz, url_prefix="/healthz")

def liveness():
    try:
        return 'liveness - OK'
    except Exception:
        raise HealthError("liveness - NO")

def readiness():
    try:
        return 'readiness - OK'
        #connect_database()
    except Exception:
        raise HealthError("readiness - NO")

app.config.update(
    HEALTHZ = {
        "live": "app.liveness",
        "ready": "app.readiness",
    }
)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)