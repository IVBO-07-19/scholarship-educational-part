import requests
from fastapi.testclient import TestClient
from main import app
import logging
import json

logging.basicConfig(level=logging.DEBUG)
client = TestClient(app)


def get_access_token():
    r = requests.post('https://suroegin503.eu.auth0.com/oauth/token', data = {
        'grant_type':'password', 
        'username': 'testingemail@gmail.com',
        'password': 'TestPassword1_',
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

def test_get_article_writers():
    response = client.get("/api/educ_part/article_writers", headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list

def test_create_article_writer():
    response = client.post("/api/educ_part/article_writers", headers=auth_headers, data=json.dumps({
        "id": 0,
        "id_person": "ingnore_this",
        "event_name": "string",
        "prize_place": 0,
        "participation": "string",
        "date": "2021-05-13",
        "scores": 0
    }))

    assert response.status_code == 200
    body = response.json()
    assert type(body) is dict
    assert body['id_person'] == userId
