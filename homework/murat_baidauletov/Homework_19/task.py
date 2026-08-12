import requests

url = "http://objapi.course.qa-practice.com/object"


def add_new_car(url):
    body = {
        "name": "AddTestObject",
        "data": {"color": "krasny", "size": "small"}
    }

    response = requests.post(url, json=body)
    assert response.status_code == 200, 'Не создался обьект'
    id_object = response.json()['id']
    return id_object


def delete_object(url, id):
    response = requests.delete(url + '/' + str(id))
    assert response.status_code == 200, 'Не удалился обект '


def all_car(url):
    response = requests.get(url)
    print(response.json())


def car(url, id):
    response = requests.get(url + '/' + str(id))
    print(response.json())


def post_car(url):
    body = {
        "name": "MuratTest",
        "data": {"color": "krasny", "size": "small"}
    }

    response = requests.post(url, json=body)
    assert response.status_code == 200, "Объект не был успешно создан"
    response_json = response.json()
    assert response_json['name'] == body['name']
    assert response_json["data"]["color"] == body["data"]["color"]


def post_car_without_data(url):
    body = {
        "name": "MuratTest"
    }
    response = requests.post(url, json=body)
    assert response.status_code == 400


def post_car_without_name(url):
    body = {
        "data": {"color": "krasny", "size": "small"}
    }
    response = requests.post(url, json=body)
    assert response.status_code == 400


def patch_car(url):
    new_test_car_id = add_new_car(url)
    body = {
        "name": "PatchTestMurat"
    }
    response = requests.patch(url + '/' + str(new_test_car_id), json=body)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['name'] == body['name']
    delete_object(url, new_test_car_id)


def put_car(url):
    new_test_car_id = add_new_car(url)
    body = {
        "name": "PutTest",
        "data": {"color": "Putkrasny", "size": "Putsmall"}
    }
    response = requests.put(url + '/' + str(new_test_car_id), json=body)
    assert response.status_code == 200
    assert response.json()['name'] == body['name']
    assert response.json()['data']['size'] == body['data']['size']
    delete_object(url, new_test_car_id)


def delete_car(url):
    new_test_car_id = add_new_car(url)
    response = requests.delete(url + '/' + str(new_test_car_id))
    assert response.status_code == 200


post_car(url)
post_car_without_name(url)
post_car_without_data(url)
put_car(url)
patch_car(url)
delete_car(url)
