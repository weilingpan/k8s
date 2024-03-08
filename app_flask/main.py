from flask import Flask, request, jsonify, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from middleware import record_request, record_response

app = Flask(__name__)


app.before_request(record_request)
app.after_request(record_response)

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/')
def index():
    return jsonify({
        'status': 'ok'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)