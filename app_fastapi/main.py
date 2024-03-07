import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Setup Prometheus metrics
Instrumentator().instrument(app).expose(app)

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