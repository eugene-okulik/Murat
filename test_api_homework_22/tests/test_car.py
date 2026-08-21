import allure
import pytest

POSITIVE = [
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
]

NEGATIVE = [
    {
        "name": "MuratTest"
    },
    {
        "data": {"color": "krasny", "size": "small"}
    },
]


@allure.feature("Создание объекта")
@allure.story("Успешное создание объекта")
@allure.title("Создание нового объекта")
@pytest.mark.parametrize("body", POSITIVE)
def test_post_car(body, create_car_endpoint):
    create_car_endpoint.create_new_car(body=body)
    create_car_endpoint.check_status_code(200)
    create_car_endpoint.check_response_data(body)


@allure.feature("Создание объекта")
@allure.story("Неуспешное создание объекта")
@allure.title("Создание объекта с невалидными данными")
@pytest.mark.parametrize("body", NEGATIVE)
def test_post_car_invalid_body(body, create_car_endpoint):
    create_car_endpoint.create_new_car(body=body)
    create_car_endpoint.check_status_code(400)


@allure.feature("Изменение объекта")
@allure.story("Полное изменение объекта")
@allure.title("Полное изменение объекта через PUT")
@pytest.mark.medium
def test_put_car(new_car, update_car_endpoint):
    body = {
        "name": "PutTest",
        "data": {"color": "Putkrasny", "size": "Putsmall"}
    }
    update_car_endpoint.update_car(object_id=new_car, body=body)
    update_car_endpoint.check_status_code(200)
    update_car_endpoint.check_response_data(body)


@allure.feature("Получение объекта")
@allure.story("Получение объекта по ID")
@allure.title("Получение существующего объекта")
def test_get_car(new_car, get_car_endpoint):
    get_car_endpoint.get_car(object_id=new_car)
    get_car_endpoint.check_object_id(new_car)
    get_car_endpoint.check_status_code(200)


@allure.feature("Удаление объекта")
@allure.story("Успешное удаление объекта")
@allure.title("Удаление существующего объекта")
def test_delete_car(new_car, delete_car_endpoint):
    delete_car_endpoint.delete_car(object_id=new_car)
    delete_car_endpoint.check_status_code(200)
