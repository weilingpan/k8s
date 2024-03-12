import os
from flask import Flask, request, jsonify, Response, send_from_directory
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from middleware import record_request, record_response, handle_exception
from utils.logger import keep_log

app = Flask(__name__)
logger = keep_log()

app.before_request(record_request)
app.after_request(record_response)
app.errorhandler(Exception)(handle_exception)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/metrics')
def metrics():
    logger.info("This is an /metrics")
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/')
def index():
    logger.info("This is an /")
    return jsonify({
        'status': 'ok'
    })

@app.get("/error")
def error():
    logger.info("This is an /error")
    raise ValueError("An example exception")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)