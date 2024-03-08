import uvicorn
from fastapi import FastAPI, Response
# from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

from middleware import PrometheusMiddleware, metrics

app = FastAPI()

# Setup Prometheus metrics
# Instrumentator().instrument(app).expose(app)

# Setting metrics middleware
app.add_middleware(PrometheusMiddleware, app_name="myfastapi")

@app.get('/metrics')
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/hello")
async def root():
    return {"message": "Hello, World!"}

@app.get("/test")
async def test():
    return {"test": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #uvicorn main:app --reload
    #conda env export > environment.yml