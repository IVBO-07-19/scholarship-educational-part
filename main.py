import configparser

import psycopg2
from fastapi import FastAPI
from psycopg2.extras import RealDictCursor

from appendix_models import *

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8-sig')

con = psycopg2.connect(
    database=config.get('postgres', 'database'),
    user=config.get('postgres', 'user'),
    password=config.get('postgres', 'password'),
    host=config.get('postgres', 'host'),
    port=int(config.get('postgres', 'port'))
)

cur = con.cursor(cursor_factory=RealDictCursor)

app = FastAPI()


@app.get('/api/educ_part/article_writers')
async def get_all_article_writers():
    cur.execute('select * from article_writers')
    if cur is not None:
        return cur.fetchall()
    else:
        return None


@app.post('/api/educ_part/article_writers')
async def create_new_article_writer(article_writer: ArticleWriter):
    cur.execute('''insert into article_writers(id_person, event_name, prize_place, participation, date, scores) 
                    values(%s,%s,%s,%s,%s,%s)''',
                (article_writer.id_person,
                 article_writer.event_name,
                 article_writer.prize_place,
                 article_writer.participation,
                 article_writer.date,
                 article_writer.scores))
    con.commit()
    cur.execute('SELECT MAX(id) FROM article_writers WHERE id is not null')
    article_writer.id = cur.fetchone()['max']
    return article_writer


@app.get('/api/educ_part/excellent_students')
async def get_all_excellent_students():
    cur.execute('select * from excellent_students')
    if cur is not None:
        return cur.fetchall()
    else:
        return None


@app.post('/api/educ_part/excellent_students')
async def create_new_excellent_student(excellent_student: ExcellentStudent):
    cur.execute('''insert into excellent_students(id_person, is_excellent) 
                    values(%s,%s)''',
                (excellent_student.id_person,
                 excellent_student.is_excellent))
    con.commit()
    cur.execute('SELECT MAX(id) FROM excellent_students WHERE id is not null')
    excellent_student.id = cur.fetchone()['max']
    return excellent_student


@app.get('/api/educ_part/olympiad_winners')
async def get_all_olympiad_winner():
    cur.execute('select * from olympiad_winners')
    if cur is not None:
        return cur.fetchall()
    else:
        return None


@app.post('/api/educ_part/olympiad_winners')
async def create_new_olympiad_winner(olympiad_winners: OlympiadWinner):
    cur.execute('''insert into olympiad_winners(id_person, event_name, level, prize_place, participation, date, scores) 
                    values(%s,%s,%s,%s,%s,%s,%s)''',
                (olympiad_winners.id_person,
                 olympiad_winners.event_name,
                 olympiad_winners.level,
                 olympiad_winners.prize_place,
                 olympiad_winners.participation,
                 olympiad_winners.date,
                 olympiad_winners.scores))
    con.commit()
    cur.execute('SELECT MAX(id) FROM olympiad_winners WHERE id is not null')
    olympiad_winners.id = cur.fetchone()['max']
    return olympiad_winners

# @app.get("/api/educ_part/example/{id}")
# async def get_object(id: int):
#     cur.execute("select * from object where id = %s", [id])
#     if cur is not None:
#         return cur.fetchall()
#     else:
#         return "No object found"
#
#
# @app.patch("/api/educ_part/example/{id}")
# async def update_object(object: Object, id:int):
#     cur.execute("update object set field1 = %s, field2 = %s where object.id = %s", (object.field1, object.field2, id))
#     con.commit()
#     cur.execute("select * from object where id = %s", [id])
#     if cur is not None:
#         return cur.fetchall()
#     else:
#         return "No object found"
#
# @app.post("/api/educ_part/example")
# async def put_object(object: Object):
#     cur.execute("insert into object(field1, field2) values(%s, %s)", (object.field1, object.field2))
#     con.commit()
#     cur.execute("select * from object")
#     if cur is not None:
#         return cur.fetchall()
#     else:
#         return "No objects"
#
# @app.delete("/api/educ_part/example/id")
# async def delete_object(id: int):
#     cur.execute("delete from object where id = %s", [id])
#     con.commit()
#     cur.execute("select * from object")
#     if cur is not None:
#         return cur.fetchall()
#     else:
#         return "No objects"
