#from flask import Flask
import http.server
from prometheus_client import Counter, start_http_server
#import prometheus_client as prom
#import random
#import time

REQUESTS = Counter('server_requests_total', 'Total HTTP Request')
EXCEPTIONS = Counter('http_exceptions_total', 'Total HTTP Exceptions')

#app = Flask(__name__)

#counter = prom.Counter('python_my_counter', 'Counter')
#gauge = prom.Gauge('python_my_gauge', 'Gauge')
#histogram = prom.Histogram('python_my_histogram', 'Histogram')
#summary = prom.Summary('python_my_summary', 'Ssummary')


#@summary.time()
#def process_request(t):
#    print(t)
#    time.sleep(t)

#@app.route('/')
#def hello():
#    return 'Hello, World!'

READY = False

class ServerHandler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):

    REQUESTS.inc()

        if self.path == '/health':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/ready':
            if READY:
                self.send_response(HTTPStatus.OK)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'READY')
            else:
                self.send_response(HTTPStatus.SERVICE_UNAVAILABLE)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'NOT READY')
        else:
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello World!')

if __name__ == '__main__':
    start_http_server(8000)
    READY = True
    server = http.server.HTTPServer(('', 5000), ServerHandler)
    server.serve_forever()
#    app.run(host='0.0.0.0', port=5000)
#    while True:
#        pass
#        counter.inc(random.random())
#        gauge.set(random.random() * 15 - 5)
#        histogram.observe(random.random() * 10)
#        summary.observe(random.random() * 10)
#        process_request(random.random() * 5)
#        time.sleep(1)