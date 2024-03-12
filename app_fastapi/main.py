import uvicorn
from fastapi import FastAPI, Response
# from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

from utils.logger import keep_log
from middleware import PrometheusMiddleware, metrics

app = FastAPI()
logger = keep_log()

# Setup Prometheus metrics
# Instrumentator().instrument(app).expose(app)

# Setting metrics middleware
app.add_middleware(PrometheusMiddleware, app_name="myfastapi")

@app.get('/metrics')
async def metrics():
    logger.info("This is an /metrics")
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/hello")
async def root():
    return {"message": "Hello, World!"}

@app.get("/test")
async def test():
    logger.info("This is an /test")
    return {"test": "ok"}

@app.get("/error")
async def error():
    return {"test": "error"}

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, workers=2)
    #python main.py
    #conda env export > environment.yml