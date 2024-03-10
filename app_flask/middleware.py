import time
from flask import request
from opentelemetry import trace
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from prometheus_client import REGISTRY, Counter, Gauge, Histogram

INFO = Gauge(
    "my_app_info", "Flask application information.", [
        "app_name"]
)
REQUESTS = Counter(
    "my_requests_total", "Total count of requests by method and path.", [
        "method", "path", "app_name"]
)
RESPONSES = Counter(
    "my_responses_total",
    "Total count of responses by method, path and status codes.",
    ["method", "path", "status_code", "app_name"],
)
REQUESTS_PROCESSING_TIME = Histogram(
    "my_requests_duration_seconds",
    "Histogram of requests processing time by path (in seconds)",
    ["method", "path", "app_name"],
)
EXCEPTIONS = Counter(
    "my_exceptions_total",
    "Total count of exceptions raised by path and exception type",
    ["method", "path", "exception_type", "app_name"],
)
REQUESTS_IN_PROGRESS = Gauge(
    "my_requests_in_progress",
    "Gauge of requests by method and path currently being processed",
    ["method", "path", "app_name"],
)

app_name = "myflask"

# def handle_exception(e):
#     method = request.method
#     path = request.path
#     EXCEPTIONS.labels(method=method, path=path, exception_type=type(
#         e).__name__, app_name=app_name).inc()

def record_request():
    request.path = request.path
    method = request.method

    REQUESTS_IN_PROGRESS.labels(
            method=method, path=request.path, app_name=app_name).inc()
    REQUESTS.labels(method=method, path=request.path, app_name=app_name).inc()
    before_time = time.perf_counter()
    request.before_time = before_time

def record_response(response):
    method = request.method
    path = request.path
    status_code = response.status_code
    
    if status_code == 200:
        after_time = time.perf_counter()
        span = trace.get_current_span()
        trace_id = trace.format_trace_id(
            span.get_span_context().trace_id)

        REQUESTS_PROCESSING_TIME.labels(method=method, 
                                        path=path, 
                                        app_name=app_name).observe(
                after_time - request.before_time, exemplar={'TraceID': trace_id}
            )
    
    RESPONSES.labels(method=method, path=path,
                     status_code=status_code,
                     app_name=app_name).inc()
    REQUESTS_IN_PROGRESS.labels(
        method=method, path=path, app_name=app_name).dec()
    return response