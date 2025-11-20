from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health_check")
def health_check():
    return "FastAPI is running properly"


class temp2(BaseModel):
    data1 : str
    data2 : float
    data3 : str


@app.post("temp4")
def temp4(dummy: temp2):
    return{
        "my_data": dummy
    }



@app.get("/temp5/{items}")
def temp5(items:str):
    return{
        "path_params": items
    }



@app.get("/temp6")
def temp6(items2:str):
    return{
        "query_params": items2
    }


@app.get("/temp7/{items3}")
def temp7(items3: str, item_price: float):
    return{
        "return_param1": items3,
        "return_param2": item_price
    }