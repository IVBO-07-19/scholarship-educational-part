from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

con = psycopg2.connect(
     database='educational_part',
     user='postgres',
     password='admin',
     host='127.0.0.1',
     port=5432
)

cur = con.cursor(cursor_factory=RealDictCursor)

class Object(BaseModel):
    field1: str
    field2: str

app = FastAPI()

@app.get("/api/educ_part/example")
async def get_objects():
    cur.execute("select * from object")
    if cur is not None:
        return cur.fetchall()
    else:
        return "No objects"


@app.get("/api/educ_part/example/{id}")
async def get_object(id: int):
    cur.execute("select * from object where id = %s", [id])
    if cur is not None:
        return cur.fetchall()
    else:
        return "No object found"


@app.patch("/api/educ_part/example/{id}")
async def update_object(object: Object, id:int):
    cur.execute("update object set field1 = %s, field2 = %s where object.id = %s", (object.field1, object.field2, id))
    con.commit()
    cur.execute("select * from object where id = %s", [id])
    if cur is not None:
        return cur.fetchall()
    else:
        return "No object found"

@app.post("/api/educ_part/example")
async def put_object(object: Object):
    cur.execute("insert into object(field1, field2) values(%s, %s)", (object.field1, object.field2))
    con.commit()
    cur.execute("select * from object")
    if cur is not None:
        return cur.fetchall()
    else:
        return "No objects"

@app.delete("/api/educ_part/example/id")
async def delete_object(id: int):
    cur.execute("delete from object where id = %s", [id])
    con.commit()
    cur.execute("select * from object")
    if cur is not None:
        return cur.fetchall()
    else:
        return "No objects"
