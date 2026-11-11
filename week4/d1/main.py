from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, API"}


@app.get("/v1/health")
def read_health():
        return {"status": "ok"}
