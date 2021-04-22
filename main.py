import configparser
import os

import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List
from fastapi_auth0 import Auth0, Auth0User

from fastapi import Depends, FastAPI, Security
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
auth0_domain = os.getenv('AUTH0_DOMAIN', 'dev-d82kol56.us.auth0.com')
auth0_api_audience = os.getenv('AUTH0_API_AUDIENCE', 'fastapi')

auth = Auth0(domain=auth0_domain, api_audience=auth0_api_audience, scopes={
    'read:blabla': 'Read BlaBla resource'
})
app = FastAPI()


# @app.get("/public")
# async def get_public():
#     return {"message": "Anonymous user"}


# @app.get("/secure", dependencies=[Depends(auth.implicit_scheme)])
# async def get_secure(user: Auth0User = Security(auth.get_user)):
#     return {"message": f"{user}"}


# @app.get("/secure/blabla", dependencies=[Depends(auth.implicit_scheme)])
# async def get_secure_scoped(user: Auth0User = Security(auth.get_user, scopes=["read:blabla"])):
#     return {"message": f"{user}"}
#
#
# @app.get("/secure/blabla2")
# async def get_secure_scoped2(user: Auth0User = Security(auth.get_user, scopes=["read:blabla"])):
#     return {"message": f"{user}"}


'''Получатель награды (приза) в течение 1-ого года, 
предшествующего назначению повышенной государственной академической
стипендии, за результаты проектной деятельности и (или) опытно-конструкторской работы'''


@app.get('/api/educ_part/article_writers', response_model=List[ArticleWriter], dependencies=[Depends(auth.implicit_scheme)])
async def get_all_article_writers(user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from article_writers')
    if cur is not None:
        return cur.fetchall()
    else:
        return None


@app.post('/api/educ_part/article_writers', response_model=ArticleWriter, dependencies=[Depends(auth.implicit_scheme)])
async def create_new_article_writer(article_writer: ArticleWriter, user: Auth0User = Security(auth.get_user)):
    cur.execute('''insert into article_writers(
                    id_person,
                    event_name,
                    prize_place,
                    participation,
                    date,
                    scores) 
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


@app.get('/api/educ_part/article_writers/{id}', response_model=ArticleWriter, dependencies=[Depends(auth.implicit_scheme)])
async def get_article_writer(id: int, user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from article_writers where id=%s', [id])
    if cur is not None:
        return cur.fetchone()
    else:
        return None


@app.put('/api/educ_part/article_writers/{id}', response_model=ArticleWriter, dependencies=[Depends(auth.implicit_scheme)])
async def update_article_writer(id: int, article_writer: ArticleWriter, user: Auth0User = Security(auth.get_user)):
    cur.execute('select id_person from article_writers where id=%s', [id])
    id_person = cur.fetchone()['id_person']
    cur.execute('''update article_writers set
        event_name = %s,
        prize_place = %s,
        participation = %s,
        date = %s,
        scores = %s
        where id = %s''', (
        article_writer.event_name,
        article_writer.prize_place,
        article_writer.participation,
        article_writer.date,
        article_writer.scores,
        id))
    con.commit()
    article_writer.id = id
    article_writer.id_person = id_person
    return article_writer


@app.delete('/api/educ_part/article_writers/{id}', response_model=ArticleWriter, dependencies=[Depends(auth.implicit_scheme)])
async def delete_article_writer(id: int, user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from article_writers where id=%s', [id])
    article_writer = cur.fetchone()
    cur.execute('delete from article_writers where id=%s', [id])
    con.commit()
    return article_writer


'''Получение в течение не менее 2-х следующих друг за другом 
промежуточных аттестаций, предшествующих назначению
повышенной государственной академической стипендии, только оценок «отлично»'''


@app.get('/api/educ_part/excellent_students', response_model=List[ExcellentStudent], dependencies=[Depends(auth.implicit_scheme)])
async def get_all_excellent_students(user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from excellent_students')
    if cur is not None:
        return cur.fetchall()
    else:
        return None


@app.post('/api/educ_part/excellent_students', response_model=ExcellentStudent, dependencies=[Depends(auth.implicit_scheme)])
async def create_new_excellent_student(excellent_student: ExcellentStudent, user: Auth0User = Security(auth.get_user)):
    cur.execute('''insert into excellent_students(id_person, excellent) 
                    values(%s,%s)''',
                (excellent_student.id_person,
                 excellent_student.excellent))
    con.commit()
    cur.execute('SELECT MAX(id) FROM excellent_students WHERE id is not null')
    excellent_student.id = cur.fetchone()['max']
    return excellent_student


@app.get('/api/educ_part/excellent_students/{id}', response_model=ExcellentStudent, dependencies=[Depends(auth.implicit_scheme)])
async def get_excellent_student(id: int, user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from excellent_students where id=%s', [id])
    if cur is not None:
        return cur.fetchone()
    else:
        return None


@app.put('/api/educ_part/excellent_students/{id}', response_model=ExcellentStudent, dependencies=[Depends(auth.implicit_scheme)])
async def update_excellent_student(id: int, excellent_student: ExcellentStudent, user: Auth0User = Security(auth.get_user)):
    cur.execute('select id_person from excellent_students where id=%s', [id])
    id_person = cur.fetchone()['id_person']
    cur.execute('''update excellent_students set
        excellent = %s
        where id = %s''', (
        excellent_student.excellent,
        id))
    con.commit()
    excellent_student.id = id
    excellent_student.id_person = id_person
    return excellent_student


@app.delete('/api/educ_part/excellent_students/{id}', response_model=ExcellentStudent, dependencies=[Depends(auth.implicit_scheme)])
async def delete_excellent_student(id: int, user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from excellent_students where id=%s', [id])
    excellent_student = cur.fetchone()
    cur.execute('delete from excellent_students where id=%s', [id])
    con.commit()
    return excellent_student


'''Победитель или призер международной, всероссийской,
ведомственной или региональной олимпиады, конкурса, соревнования,
состязания или иного мероприятия, направленных на выявление учебных достижений студентов,
проведенных в течение 1-ого года,
предшествующего назначению повышенной государственной академической:'''


@app.get('/api/educ_part/olympiad_winners', response_model=List[OlympiadWinner], dependencies=[Depends(auth.implicit_scheme)])
async def get_all_olympiad_winners(user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from olympiad_winners')
    if cur is not None:
        return cur.fetchall()
    else:
        return None


@app.post('/api/educ_part/olympiad_winners', response_model=OlympiadWinner, dependencies=[Depends(auth.implicit_scheme)])
async def create_new_olympiad_winner(olympiad_winners: OlympiadWinner, user: Auth0User = Security(auth.get_user)):
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


@app.get('/api/educ_part/olympiad_winners/{id}', response_model=OlympiadWinner, dependencies=[Depends(auth.implicit_scheme)])
async def get_olympiad_winner(id: int, user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from olympiad_winners where id=%s', [id])
    if cur is not None:
        return cur.fetchone()
    else:
        return None


@app.put('/api/educ_part/olympiad_winners/{id}', response_model=OlympiadWinner, dependencies=[Depends(auth.implicit_scheme)])
async def update_olympiad_winner(id: int, olympiad_winner: OlympiadWinner, user: Auth0User = Security(auth.get_user)):
    cur.execute('select id_person from olympiad_winners where id=%s', [id])
    id_person = cur.fetchone()['id_person']
    cur.execute('''update olympiad_winners set
        event_name = %s,
        level = %s,
        prize_place = %s,
        participation = %s,
        date = %s,
        scores = %s
        where id = %s''', (
        olympiad_winner.event_name,
        olympiad_winner.level,
        olympiad_winner.prize_place,
        olympiad_winner.participation,
        olympiad_winner.date,
        olympiad_winner.scores,
        id))
    con.commit()
    olympiad_winner.id = id
    olympiad_winner.id_person = id_person
    return olympiad_winner


@app.delete('/api/educ_part/olympiad_winners/{id}', response_model=OlympiadWinner, dependencies=[Depends(auth.implicit_scheme)])
async def delete_olympiad_winner(id: int, user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from olympiad_winners where id=%s', [id])
    olympiad_winner = cur.fetchone()
    cur.execute('delete from olympiad_winners where id=%s', [id])
    con.commit()
    return olympiad_winner
