import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'

ENDPOINT = 'api/serialize/listview'


def get_update(id=None):
    in_data = json.dumps({})
    if id is not None:
        in_data = json.dumps({
            'id': id
        })

    r = requests.get(BASE_URL + ENDPOINT, data=in_data)
    data = r.json()
    print(data)


def create_update():
    new_data = {
        'user': 1,
        'content': 'another update'
    }

    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.headers)
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()
    print(r.text)


def update_update():

    new_data = {
        'content': 'Thats what we are talking about'
    }
    r = requests.put(BASE_URL + ENDPOINT + '/3', data=json.dumps(new_data))
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()
    print(r.text)


def delete_update(id='2'):
    new_data = {
        'id': id
    }
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(r.status_code)
    print(r.json())


delete_update()
