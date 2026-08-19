import requests
import pytest
import allure

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
def new_car():
    body = {
        "name": "MuratTest",
        "data": {"color": "krasny", "size": "small"}
    }

    with allure.step("Создать объект перед тестом"):
        response = requests.post(URL, json=body)
        assert response.status_code == 200, "Не создался объект"
        id_object = response.json()["id"]

    yield id_object

    with allure.step("Проверить, существует ли объект после теста"):
        get_response = requests.get(f"{URL}/{id_object}")

    if get_response.status_code == 200:
        with allure.step("Удалить объект после теста"):
            delete_response = requests.delete(f"{URL}/{id_object}")
            assert delete_response.status_code == 200, "Не удалился объект"


@allure.feature("Создание объекта")
@allure.story("Успешное создание объекта")
@allure.title("Создание нового объекта")
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
    with allure.step("Отправляем пост запрос"):
        response = requests.post(URL, json=body)
    with allure.step("Проверяем статус кода"):
        assert response.status_code == 200, "Объект не был успешно создан"
    with allure.step("Проверить данные созданного объекта"):
        response_json = response.json()
        assert response_json['name'] == body['name']
        assert response_json["data"]["color"] == body["data"]["color"]


@allure.feature("Создание объекта")
@allure.story("Негативный тест.Создание объекта без обязательного поля data")
@allure.title("Создание объекта без поля data")
def test_post_car_without_data():
    body = {
        "name": "MuratTest"
    }
    with allure.step("Отправить POST запрос без поля data"):
        response = requests.post(URL, json=body)
    with allure.step("Проверить статус код 400"):
        assert response.status_code == 400


@allure.feature("Создание объекта")
@allure.story("Негативный тест. Создание объекта без обязательного поля name")
@allure.title("Создание объекта без поля name")
def test_post_car_without_name():
    body = {
        "data": {"color": "krasny", "size": "small"}
    }
    with allure.step("Отправить POST запрос без поля name"):
        response = requests.post(URL, json=body)

    with allure.step("Проверить статус код 400"):
        assert response.status_code == 400


@allure.feature("Изменение объекта")
@allure.story("Частичное изменение объекта")
@allure.title("Изменение имени объекта через PATCH")
@pytest.mark.critical
def test_patch_car(new_car):
    body = {
        "name": "PatchTestMurat"
    }
    with allure.step("Отправить PATCH запрос с новым именем"):
        response = requests.patch(
            URL + "/" + str(new_car),
            json=body
        )
    with allure.step("Проверить статус код 200"):
        assert response.status_code == 200

    with allure.step("Проверить измененное имя объекта"):
        response_json = response.json()
        assert response_json["name"] == body["name"]


@allure.feature("Изменение объекта")
@allure.story("Полное изменение объекта")
@allure.title("Полное изменение объекта через PUT")
@pytest.mark.medium
def test_put_car(new_car):
    body = {
        "name": "PutTest",
        "data": {"color": "Putkrasny", "size": "Putsmall"}
    }
    with allure.step("Отправить PUT запрос с новыми данными"):
        response = requests.put(
            URL + "/" + str(new_car),
            json=body
        )

    with allure.step("Проверить статус код 200"):
        assert response.status_code == 200

    with allure.step("Проверить поля объекта"):
        assert response.json()["name"] == body["name"]
        assert response.json()['data']['size'] == body['data']['size']


@allure.feature("Удаление объекта")
@allure.story("Успешное удаление объекта")
@allure.title("Удаление существующего объекта")
def test_delete_car(new_car):
    with allure.step("Отправить DELETE запрос"):
        response = requests.delete(
            URL + "/" + str(new_car)
        )

    with allure.step("Проверить статус код 200"):
        assert response.status_code == 200
