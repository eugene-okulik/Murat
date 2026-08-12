import requests
import pytest

URL = "http://objapi.course.qa-practice.com/object"


@pytest.fixture(scope='session', autouse=True)
def start_completed():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function', autouse=True)
def before_after():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def add_del_new_car():
    body = {
        "name": "MuratTest",
        "data": {"color": "krasny", "size": "small"}
    }
    response = requests.post(URL, json=body)
    assert response.status_code == 200, 'Не создался обьект'
    id_object = response.json()['id']
    yield id_object
    response = requests.delete(URL + '/' + str(id_object))
    assert response.status_code == 200, 'Не удалился обект '


@pytest.fixture()
def add_new_car():
    body = {
        "name": "MuratTest",
        "data": {"color": "krasny", "size": "small"}
    }
    response = requests.post(URL, json=body)
    assert response.status_code == 200, 'Не создался обьект'
    return response.json()['id']


@pytest.mark.parametrize("body", [
    {
        "name": "MuratTest",
        "data": {
            "color": "krasny",
            "size": "small"
        }
    },
    {
        "name": "MuratTest",
        "data": {
            "color": "jelti",
            "size": "big"
        }
    },
    {
        "name": "MuratTest",
        "data": {
            "color": "zeleni",
            "size": "zanijenny"
        }
    },
])
def test_post_car(body):
    response = requests.post(URL, json=body)
    assert response.status_code == 200, "Объект не был успешно создан"
    response_json = response.json()
    assert response_json['name'] == body['name']
    assert response_json["data"]["color"] == body["data"]["color"]


def test_post_car_without_data():
    body = {
        "name": "MuratTest"
    }
    response = requests.post(URL, json=body)
    assert response.status_code == 400


def test_post_car_without_name():
    body = {
        "data": {"color": "krasny", "size": "small"}
    }
    response = requests.post(URL, json=body)
    assert response.status_code == 400


@pytest.mark.critical
def test_patch_car(add_del_new_car):
    body = {
        "name": "PatchTestMurat"
    }
    response = requests.patch(URL + '/' + str(add_del_new_car), json=body)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['name'] == body['name']


@pytest.mark.medium
def test_put_car(add_del_new_car):
    body = {
        "name": "PutTest",
        "data": {"color": "Putkrasny", "size": "Putsmall"}
    }
    response = requests.put(URL + '/' + str(add_del_new_car), json=body)
    assert response.status_code == 200
    assert response.json()['name'] == body['name']
    assert response.json()['data']['size'] == body['data']['size']


def test_delete_car(add_new_car):
    response = requests.delete(URL + '/' + str(add_new_car))
    assert response.status_code == 200
