import json
from time import sleep
import requests
import pytest
from datetime import date
import urllib



endpoint = "http://nginx/api/v1/"
# data = {"ip": "1.1.2.3"}
# headers = {"Authorization": "Bearer MYREALLYLONGTOKENIGOT"}

# headers={"WWW-Authenticate": "Bearer"}


def test_all():
    # данные для теста
    testdata = {
        "username": "<<neverusedbyanyone_testname>>",
        "password": "<<neverusedbyanyone_testpassword>>",
        "zp": 150000,
        "growdate": str(date.today()),
    }

    goagain = True
    while goagain:
        api = requests.get(url='http://nginx/')
        if api.status_code == 200:
            goagain = False
        else:
            sleep(1)

    # получение всех пользователей
    data, headers = None, None
    api = requests.get(url=endpoint + 'user/', data=data, headers=headers)
    assert api.status_code == 200
    assert type(api.json()) == list

    # новый пользователь
    data = testdata
    api = requests.post(url=endpoint + 'user/', data=json.dumps(data), headers=headers)
    assert api.status_code == 200
    assert type(api.json()) == dict

    # имена пользователей уникальны
    api = requests.post(url=endpoint + 'user/', data=json.dumps(data), headers=headers)
    assert api.status_code == 500

    # получить токен и id
    data = {
        "username": testdata["username"],
        "password": testdata["password"],
    }
    data = urllib.parse.urlencode(data)
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    api = requests.post(url=endpoint + 'auth/token', data=data, headers=headers)
    assert api.status_code == 200
    assert type(api.json()) == dict

    token = api.json()['access_token']
    id = api.json()['user_id']

    # получаем данные по айди и токену
    headers = {"Authorization": f"Bearer {token}"}
    data = None
    api = requests.get(url=endpoint + f'user/{id}', data=data, headers=headers)
    assert api.status_code == 200
    assert type(api.json()) == dict

    newtestdata = {
        "username": "<<neverusedbyanyone_onemore>>",
        "password": "<<neverusedbyanyone_testonemore>>",
        "zp": 200000,
        "growdate": str(date.today()),
    }

    # меняем данные пользователя
    headers = {"Authorization": f"Bearer {token}"}
    data = json.dumps(newtestdata)
    api = requests.post(url=endpoint + f'user/{id}/update', data=data, headers=headers)
    assert api.status_code == 200
    assert type(api.json()) == dict

    # удаляем пользователя
    headers = {"Authorization": f"Bearer {token}"}
    data = None
    api = requests.get(url=endpoint + f'user/{id}/delete', data=data, headers=headers)
    assert api.status_code == 200
    assert type(api.json()) == str
