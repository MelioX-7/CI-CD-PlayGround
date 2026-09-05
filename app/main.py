from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "CI/CD Playground is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}
