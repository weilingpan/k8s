from flask import Flask, request, jsonify, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from middleware import record_request, record_response, app_name, EXCEPTIONS

app = Flask(__name__)


app.before_request(record_request)
app.after_request(record_response)

@app.errorhandler(Exception)
def handle_exception(e):
    path = request.path
    method = request.method
    EXCEPTIONS.labels(method=method, path=path, exception_type=type(
                e).__name__, app_name=app_name).inc()
    
    response = {
        "message": "An error occurred",
        "error": str(e),
        "path": path
    }
    return jsonify(response), 500

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/')
def index():
    return jsonify({
        'status': 'ok'
    })

@app.get("/error")
def error():
    raise ValueError("An example exception")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)