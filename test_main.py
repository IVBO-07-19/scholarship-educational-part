import json

import requests
from fastapi.testclient import TestClient
import appendix_models

from main import app

client = TestClient(app)


def get_access_token():
    r = requests.post('https://suroegin503.eu.auth0.com/oauth/token', data={
        'grant_type': 'password',
        'username': 'student@mirea.ru',
        'password': '123',
        'scope': 'openid profile email',
        'audience': 'https://welcome/',
        'client_id': 'PdkS09Ig0EYVGK9KPYwncjKMGzXnAasI'})
    return r.json()['access_token']


token = get_access_token()

auth_headers = {'Authorization': f'Bearer {token}'}


def get_user_id():
    r = requests.get('https://suroegin503.eu.auth0.com/userinfo', headers=auth_headers)
    return r.json()['sub']


userId = get_user_id()


def test_not_authorized():
    response = client.get("/api/educ_part/article_writers")
    assert response.status_code == 401 or response.status_code == 403


###################################################
###################################################
###################################################
###################################################

def test_get_article_writers():
    response = client.get("/api/educ_part/article_writers", headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list


def test_create_article_writer_user_id():
    response = client.post("/api/educ_part/article_writers", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "id_person": "ingnore_this",
        "event_name": "string",
        "prize_place": 1,
        "participation": "string",
        "date": "2021-05-13",
        "scores": 0
    }))

    assert response.status_code == 200
    body = response.json()
    assert type(body) is dict
    assert body['id_person'] == userId
    assert body['event_name'] == 'string'
    assert body['prize_place'] == 1
    assert body['participation'] == 'string'
    assert body['scores'] == 0


def test_create_article_writer_with_incorrect_place_returns_400():
    response = client.post("/api/educ_part/article_writers", headers=auth_headers, data=json.dumps({
        "id": 0,
        "event_name": "string",
        "prize_place": -1,
        "participation": "string",
        "date": "2021-05-13",
        "scores": 0
    }))

    assert response.status_code // 100 == 4


def test_get_article_writer_with_incorrect_id():
    response = client.get("/api/educ_part/article_writers/45", headers=auth_headers)
    assert response.status_code // 100 == 4


def test_get_article_writers_with_id():
    response = client.post("/api/educ_part/article_writers", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "event_name": "string",
        "prize_place": 2,
        "participation": "string",
        "date": "2021-05-13",
        "scores": 0
    }))
    tmp_id = response.json()['id']
    response = client.get("/api/educ_part/article_writers/" + str(tmp_id), headers=auth_headers)
    assert response.status_code // 100 == 2


def test_delete_article_writers_with_incorrect_id():
    response = client.delete("/api/educ_part/article_writers/607", headers=auth_headers)
    assert response.status_code // 100 == 4


def test_delete_article_writers():
    response = client.post("/api/educ_part/article_writers", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "event_name": "string",
        "prize_place": 2,
        "participation": "string",
        "date": "2021-05-13",
        "scores": 0
    }))
    assert response.status_code // 100 == 2
    tmp_id = response.json()['id']
    response = client.delete("/api/educ_part/article_writers/" + str(tmp_id), headers=auth_headers)
    assert response.json()['id'] == tmp_id
    assert response.status_code // 100 == 2
    response = client.get("/api/educ_part/article_writers/" + str(tmp_id), headers=auth_headers)
    assert response.status_code // 100 == 4


def test_update_article_writer_with_correct_id():
    response = client.post("/api/educ_part/article_writers", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "event_name": "string",
        "prize_place": 2,
        "participation": "string",
        "date": "2021-05-13",
        "scores": 0
    }))
    tmp_id = response.json()['id']
    assert response.status_code // 100 == 2
    response = client.put("/api/educ_part/article_writers/" + str(tmp_id), headers=auth_headers, data=json.dumps({
        "id_application": 123,
        "event_name": "who",
        "prize_place": 6,
        "participation": "where",
        "date": "2021-05-13",
        "scores": 0
    }))
    body = response.json()
    assert body['event_name'] == 'who'
    assert body['prize_place'] == 6
    assert body['participation'] == 'where'
    assert body['scores'] == 0


#############################################
#############################################
#############################################
#############################################

def test_get_excellent_students():
    response = client.get("/api/educ_part/excellent_students", headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list


def test_create_excellent_student_user_id():
    response = client.post("/api/educ_part/excellent_students", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "id_person": "ingnore_this",
        "excellent": True
    }))

    assert response.status_code == 200
    body = response.json()
    assert type(body) is dict
    assert body['id_person'] == userId
    assert body['excellent'] == True


def test_get_excellent_students_with_incorrect_id():
    response = client.get("/api/educ_part/excellent_students/45", headers=auth_headers)
    assert response.status_code // 100 == 4


def test_get_excellent_students_with_id():
    response = client.post("/api/educ_part/excellent_students", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "id_person": "ingnore_this",
        "excellent": True
    }))
    tmp_id = response.json()['id']
    response = client.get("/api/educ_part/excellent_students/" + str(tmp_id), headers=auth_headers)
    assert response.status_code // 100 == 2


def test_delete_excellent_students_with_incorrect_id():
    response = client.delete("/api/educ_part/excellent_students/607", headers=auth_headers)
    assert response.status_code // 100 == 4


def test_delete_excellent_students():
    response = client.post("/api/educ_part/excellent_students", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "id_person": "ingnore_this",
        "excellent": True
    }))
    assert response.status_code // 100 == 2
    tmp_id = response.json()['id']
    response = client.delete("/api/educ_part/excellent_students/" + str(tmp_id), headers=auth_headers)
    assert response.json()['id'] == tmp_id
    assert response.status_code // 100 == 2
    response = client.get("/api/educ_part/excellent_students/" + str(tmp_id), headers=auth_headers)
    assert response.status_code // 100 == 4


def test_update_excellent_student_with_correct_id():
    response = client.post("/api/educ_part/excellent_students", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "id_person": "string",
        "excellent": True
    }))
    tmp_id = response.json()['id']
    assert response.status_code // 100 == 2
    response = client.put("/api/educ_part/excellent_students/" + str(tmp_id), headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "id_person": "string",
        "excellent": False
    }))
    body = response.json()
    assert not body['excellent']
    assert response.status_code // 100 == 2


##################################################
#################################################
################################################
###############################################

def test_get_olympiad_winners():
    response = client.get("/api/educ_part/olympiad_winners", headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list


def test_create_olympiad_winners_user_id():
    response = client.post("/api/educ_part/olympiad_winners", headers=auth_headers, data=json.dumps({
        "id": 1,
        "id_application": 123,
        "id_person": "hdj23JDSJLdas",
        "event_name": "Олимпиада",
        "level": "Мировой",
        "prize_place": 1,
        "participation": "Индивид",
        "date": "2021-04-17",
        "scores": 32124.23
    }))
    assert response.status_code == 200
    body = response.json()
    assert type(body) is dict
    assert body['id_person'] == userId
    assert body['event_name'] == 'Олимпиада'
    assert body['level'] == 'Мировой'
    assert body['prize_place'] == 1
    assert body['participation'] == 'Индивид'
    assert body['scores'] == 32124.23


def test_create_olympiad_winners_with_incorrect_place_returns_400():
    response = client.post("/api/educ_part/article_writers", headers=auth_headers, data=json.dumps({
        "id": 1,
        "id_person": "hdj23JDSJLdas",
        "event_name": "Олимпиада",
        "level": "Мировой",
        "prize_place": 0,
        "participation": "Индивид",
        "date": "2021-04-17",
        "scores": 32124.23
    }))

    assert response.status_code // 100 == 4


def test_get_olympiad_winners_with_incorrect_id():
    response = client.get("/api/educ_part/olympiad_winners/45", headers=auth_headers)
    assert response.status_code // 100 == 4


def test_get_olympiad_winners_with_id():
    response = client.post("/api/educ_part/olympiad_winners", headers=auth_headers, data=json.dumps({
        "id": 1,
        "id_application": 123,
        "id_person": "hdj23JDSJLdas",
        "event_name": "Олимпиада",
        "level": "Мировой",
        "prize_place": 1,
        "participation": "Индивид",
        "date": "2021-04-17",
        "scores": 32124.23
    }))
    tmp_id = response.json()['id']
    response = client.get("/api/educ_part/olympiad_winners/" + str(tmp_id), headers=auth_headers)
    assert response.status_code // 100 == 2


def test_delete_olympiad_winners_with_incorrect_id():
    response = client.delete("/api/educ_part/olympiad_winners/607", headers=auth_headers)
    assert response.status_code // 100 == 4


def test_delete_olympiad_winners():
    response = client.post("/api/educ_part/olympiad_winners", headers=auth_headers, data=json.dumps({
        "id": 1,
        "id_application": 123,
        "id_person": "hdj23JDSJLdas",
        "event_name": "Олимпиада",
        "level": "Мировой",
        "prize_place": 1,
        "participation": "Индивид",
        "date": "2021-04-17",
        "scores": 32124.23
    }))
    assert response.status_code // 100 == 2
    tmp_id = response.json()['id']
    response = client.delete("/api/educ_part/olympiad_winners/" + str(tmp_id), headers=auth_headers)
    assert response.json()['id'] == tmp_id
    assert response.status_code // 100 == 2
    response = client.get("/api/educ_part/olympiad_winners/" + str(tmp_id), headers=auth_headers)
    assert response.status_code // 100 == 4


def test_update_olympiad_winners_with_correct_id():
    response = client.post("/api/educ_part/olympiad_winners", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_application": 123,
        "id_person": "string",
        "event_name": "string",
        "level": "string",
        "prize_place": 6,
        "participation": "string",
        "date": "2021-05-27",
        "scores": 0
    }))
    tmp_id = response.json()['id']
    assert response.status_code // 100 == 2
    response = client.put("/api/educ_part/olympiad_winners/" + str(tmp_id), headers=auth_headers, data=json.dumps({
        "id_application": 123,
        "event_name": "some_event",
        "level": "some_level",
        "prize_place": 4,
        "participation": "some_participation",
        "date": "2021-05-27",
        "scores": 0
    }))
    body = response.json()
    assert body['event_name'] == 'some_event'
    assert body['level'] == 'some_level'
    assert body['prize_place'] == 4
    assert body['participation'] == 'some_participation'
    assert response.status_code // 100 == 2
