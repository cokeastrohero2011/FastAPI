from fastapi import FastAPI

app = FastAPI()

@app.get("/health_check")
def health_check():
    return "FastAPI is running properly"