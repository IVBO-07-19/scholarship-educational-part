from fastapi import FastAPI
from pydantic import BaseModel


class Object(BaseModel):
    id: int = None
    field1: str
    field2: str


app = FastAPI()

objects = []


@app.get("/api/educ_part/example")
async def get_objects():
    return objects


@app.get("/api/educ_part/example/{id}")
async def get_object(id: int):
    try:
        return objects[id - 1]
    except IndexError:
        return "No object found"


@app.post("/api/educ_part/example")
async def put_object(object: Object):
    if len(objects) != 0:
        object.id = objects[-1].id + 1
    else:
        object.id = 1
    objects.append(object)
    return objects
