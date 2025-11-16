from fastapi import FastAPI

app = FastAPI()

@app.get("/health_check")
def health_check():
    return {"message": "FastAPI is running properly"}


# path parameters

@app.get("/items/{item_id}")
def items(item_id:int):
    return {"data":f"{item_id}"}

# multiple path parameters
@app.get("/items/{item_id}/{item_name}")
def items(item_id:int, item_name:str):
    return {
        "item_name":item_name,
        "item_id": item_id
    }
