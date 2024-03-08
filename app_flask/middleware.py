from flask import request
from prometheus_client import REGISTRY, Counter, Gauge, Histogram

INFO = Gauge(
    "flask_app_info", "Flask application information.", [
        "app_name"]
)
REQUESTS = Counter(
    "flask_requests_total", "Total count of requests by method and path.", [
        "method", "path", "app_name"]
)
RESPONSES = Counter(
    "flask_responses_total",
    "Total count of responses by method, path and status codes.",
    ["method", "path", "status_code", "app_name"],
)
REQUESTS_PROCESSING_TIME = Histogram(
    "flask_requests_duration_seconds",
    "Histogram of requests processing time by path (in seconds)",
    ["method", "path", "app_name"],
)
EXCEPTIONS = Counter(
    "flask_exceptions_total",
    "Total count of exceptions raised by path and exception type",
    ["method", "path", "exception_type", "app_name"],
)
REQUESTS_IN_PROGRESS = Gauge(
    "flask_requests_in_progress",
    "Gauge of requests by method and path currently being processed",
    ["method", "path", "app_name"],
)

def record_request():
    request.handler = request.path

def record_response(response):
    method = request.method
    status = str(response.status_code // 100) + 'xx'
    path = request.handler
    RESPONSES.labels(method=method, status_code=status, path=path, app_name="myflask").inc()
    return response