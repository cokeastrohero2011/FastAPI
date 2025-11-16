from fastapi import FastAPI, Header, HTTPException, dependencies, Depends

def verify_secret_key(key = Header()):
    my_secret_key = "123"
    if key != my_secret_key:
        raise HTTPException (401, "unauthorized access")

app = FastAPI(dependencies = [Depends(verify_secret_key)])

@app.get("/health_check")
def health_check():
    return {"message": "FastAPI is running properly"}


@app.get("/items/{item_id}")
def items(item_id:int):
    return {"data":f"{item_id}"}