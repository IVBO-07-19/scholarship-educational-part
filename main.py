import configparser
import os
from typing import List

import psycopg2
from fastapi import Depends, FastAPI, Security, Response, status
from fastapi_auth0 import Auth0, Auth0User
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
auth0_domain = os.getenv('AUTH0_DOMAIN', 'suroegin503.eu.auth0.com')
auth0_api_audience = os.getenv('AUTH0_API_AUDIENCE', 'https://welcome/')

auth = Auth0(domain=auth0_domain, api_audience=auth0_api_audience, scopes={
    'read:blabla': 'Read BlaBla resource'
})

app = FastAPI()


def check_prize_place(place: int) -> bool:
    return True if place > 0 else False


'''Получатель награды (приза) в течение 1-ого года, 
предшествующего назначению повышенной государственной академической
стипендии, за результаты проектной деятельности и (или) опытно-конструкторской работы'''


@app.get('/api/educ_part/article_writers', response_model=List[ArticleWriter],
         dependencies=[Depends(auth.implicit_scheme)], status_code=status.HTTP_200_OK)
async def get_all_article_writers(user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from article_writers')
    if cur is not None:
        return cur.fetchall()
    else:
        return None


@app.post('/api/educ_part/article_writers', response_model=ArticleWriter, dependencies=[Depends(auth.implicit_scheme)])
async def create_new_article_writer(response: Response,
                                    article_writer: ArticleWriter,
                                    user: Auth0User = Security(auth.get_user)):
    if check_prize_place(article_writer.prize_place):
        cur.execute('''insert into article_writers(
                    id_person,
                    event_name,
                    prize_place,
                    participation,
                    date,
                    scores) 
                    values(%s,%s,%s,%s,%s,%s) returning id''',
                    (user.id,
                     article_writer.event_name,
                     article_writer.prize_place,
                     article_writer.participation,
                     article_writer.date,
                     article_writer.scores))
        con.commit()
        tmp_id = cur.fetchone()['id']
        cur.execute('SELECT * FROM article_writers WHERE id = %s', (tmp_id,))
        response.status_code = status.HTTP_201_CREATED
        return cur.fetchone()
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


@app.get('/api/educ_part/article_writers/{id}', response_model=ArticleWriter,
         dependencies=[Depends(auth.implicit_scheme)])
async def get_article_writer(response: Response,
                             tmp_id: int,
                             user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from article_writers where id=%s', [tmp_id])
    tmp_dict = cur.fetchone()
    if tmp_dict is not None:
        response.status_code = status.HTTP_200_OK
        return tmp_dict
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


@app.put('/api/educ_part/article_writers/{id}', response_model=ArticleWriter,
         dependencies=[Depends(auth.implicit_scheme)])
async def update_article_writer(response: Response,
                                id: int,
                                article_writer: ArticleWriter,
                                user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from article_writers where id=%s', [id])
    tmp_dict = cur.fetchone()
    if check_prize_place(article_writer.prize_place) and tmp_dict is not None:
        cur.execute('''update article_writers set
            event_name = %s,
            prize_place = %s,
            participation = %s,
            date = %s,
            scores = %s
            where id = %s returning id, id_person''', (
            article_writer.event_name,
            article_writer.prize_place,
            article_writer.participation,
            article_writer.date,
            article_writer.scores,
            id))
        con.commit()
        tmp_dict = cur.fetchone()
        article_writer.id = tmp_dict['id']
        article_writer.id_person = tmp_dict['id_person']
        response.status_code = status.HTTP_200_OK
        return article_writer
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


@app.delete('/api/educ_part/article_writers/{id}', response_model=ArticleWriter,
            dependencies=[Depends(auth.implicit_scheme)])
async def delete_article_writer(response: Response,
                                id: int,
                                user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from article_writers where id=%s', [id])
    article_writer = cur.fetchone()
    if article_writer is not None:
        cur.execute('delete from article_writers where id=%s', [id])
        con.commit()
        response.status_code = status.HTTP_200_OK
        return article_writer
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


'''Получение в течение не менее 2-х следующих друг за другом 
промежуточных аттестаций, предшествующих назначению
повышенной государственной академической стипендии, только оценок «отлично»'''


@app.get('/api/educ_part/excellent_students', response_model=List[ExcellentStudent],
         dependencies=[Depends(auth.implicit_scheme)], status_code=status.HTTP_200_OK)
async def get_all_excellent_students(user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from excellent_students')
    if cur is not None:
        return cur.fetchall()
    else:
        return None


@app.post('/api/educ_part/excellent_students', response_model=ExcellentStudent,
          dependencies=[Depends(auth.implicit_scheme)])
async def create_new_excellent_student(excellent_student: ExcellentStudent, user: Auth0User = Security(auth.get_user)):
    cur.execute('''insert into excellent_students(id_person, excellent) 
                    values(%s,%s) returning id''',
                (user.id,
                 excellent_student.excellent))
    con.commit()
    tmp_id = cur.fetchone()['id']
    cur.execute('SELECT * FROM excellent_students WHERE id = %s', (tmp_id,))
    return cur.fetchone()


@app.get('/api/educ_part/excellent_students/{id}', response_model=ExcellentStudent,
         dependencies=[Depends(auth.implicit_scheme)])
async def get_excellent_student(response: Response,
                                id: int,
                                user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from excellent_students where id=%s', [id])
    tmp_dict = cur.fetchone()
    if tmp_dict is not None:
        response.status_code = status.HTTP_200_OK
        return tmp_dict
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


@app.put('/api/educ_part/excellent_students/{id}', response_model=ExcellentStudent,
         dependencies=[Depends(auth.implicit_scheme)])
async def update_excellent_student(response: Response,
                                   id: int,
                                   excellent_student: ExcellentStudent,
                                   user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from excellent_students where id=%s', [id])
    tmp_dict = cur.fetchone()
    if tmp_dict is not None:
        cur.execute('''update excellent_students set
            excellent = %s
            where id = %s returning id, id_person''', (
            excellent_student.excellent,
            id))
        con.commit()
        tmp_dict = cur.fetchone()
        excellent_student.id = tmp_dict['id']
        excellent_student.id_person = tmp_dict['id_person']
        response.status_code = status.HTTP_200_OK
        return excellent_student
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


@app.delete('/api/educ_part/excellent_students/{id}', response_model=ExcellentStudent,
            dependencies=[Depends(auth.implicit_scheme)])
async def delete_excellent_student(response: Response,
                                   id: int,
                                   user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from excellent_students where id=%s', [id])
    excellent_student = cur.fetchone()
    if excellent_student is not None:
        cur.execute('delete from excellent_students where id=%s', [id])
        con.commit()
        response.status_code = status.HTTP_200_OK
        return excellent_student
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


'''Победитель или призер международной, всероссийской,
ведомственной или региональной олимпиады, конкурса, соревнования,
состязания или иного мероприятия, направленных на выявление учебных достижений студентов,
проведенных в течение 1-ого года,
предшествующего назначению повышенной государственной академической:'''


@app.get('/api/educ_part/olympiad_winners', response_model=List[OlympiadWinner],
         dependencies=[Depends(auth.implicit_scheme)], status_code=status.HTTP_200_OK)
async def get_all_olympiad_winners(user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from olympiad_winners')
    if cur is not None:
        return cur.fetchall()
    else:
        return None


@app.post('/api/educ_part/olympiad_winners', response_model=OlympiadWinner,
          dependencies=[Depends(auth.implicit_scheme)])
async def create_new_olympiad_winner(response: Response,
                                     olympiad_winners: OlympiadWinner,
                                     user: Auth0User = Security(auth.get_user)):
    if check_prize_place(olympiad_winners.prize_place):
        cur.execute('''insert into olympiad_winners(id_person, event_name, level, prize_place, participation, date, scores) 
                    values(%s,%s,%s,%s,%s,%s,%s) returning id''',
                    (user.id,
                     olympiad_winners.event_name,
                     olympiad_winners.level,
                     olympiad_winners.prize_place,
                     olympiad_winners.participation,
                     olympiad_winners.date,
                     olympiad_winners.scores))
        con.commit()
        tmp_id = cur.fetchone()['id']
        cur.execute('SELECT * FROM olympiad_winners WHERE id = %s', (tmp_id,))
        response.status_code = status.HTTP_201_CREATED
        return cur.fetchone()
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


@app.get('/api/educ_part/olympiad_winners/{id}', response_model=OlympiadWinner,
         dependencies=[Depends(auth.implicit_scheme)])
async def get_olympiad_winner(response: Response,
                              id: int,
                              user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from olympiad_winners where id=%s', [id])
    tmp_dict = cur.fetchone()
    if tmp_dict is not None:
        response.status_code = status.HTTP_200_OK
        return tmp_dict
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


@app.put('/api/educ_part/olympiad_winners/{id}', response_model=OlympiadWinner,
         dependencies=[Depends(auth.implicit_scheme)])
async def update_olympiad_winner(response: Response,
                                 id: int,
                                 olympiad_winner: OlympiadWinner,
                                 user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from olympiad_winners where id=%s', [id])
    tmp_dict = cur.fetchone()
    if check_prize_place(olympiad_winner.prize_place) and tmp_dict is not None:
        cur.execute('''update olympiad_winners set
            event_name = %s,
            level = %s,
            prize_place = %s,
            participation = %s,
            date = %s,
            scores = %s
            where id = %s returning id, id_person''', (
            olympiad_winner.event_name,
            olympiad_winner.level,
            olympiad_winner.prize_place,
            olympiad_winner.participation,
            olympiad_winner.date,
            olympiad_winner.scores,
            id))
        con.commit()
        tmp_dict = cur.fetchone()
        olympiad_winner.id = tmp_dict['id']
        olympiad_winner.id_person = tmp_dict['id_person']
        response.status_code = status.HTTP_200_OK
        return olympiad_winner
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None


@app.delete('/api/educ_part/olympiad_winners/{id}', response_model=OlympiadWinner,
            dependencies=[Depends(auth.implicit_scheme)])
async def delete_olympiad_winner(response: Response,
                                 id: int,
                                 user: Auth0User = Security(auth.get_user)):
    cur.execute('select * from olympiad_winners where id=%s', [id])
    olympiad_winner = cur.fetchone()
    if olympiad_winner is not None:
        cur.execute('delete from olympiad_winners where id=%s', [id])
        con.commit()
        response.status_code = status.HTTP_200_OK
        return olympiad_winner
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None