from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class OptionsAva(str, Enum):
    algo = "AlgunaPrueba"
    other = "OtherTest"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/test/{some_parameter}')
async def test(some_parameter: str):
    return {"message": f"Some parameter was {some_parameter}"}
