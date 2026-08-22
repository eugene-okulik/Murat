import pytest
from test_api_homework_22.endpoints.create_car import CreateCar
from test_api_homework_22.endpoints.update_car import UpdateCar
from test_api_homework_22.endpoints.delete_car import DeleteCar
from test_api_homework_22.endpoints.get_car import GetCar


@pytest.fixture()
def create_car_endpoint():
    return CreateCar()


@pytest.fixture()
def update_car_endpoint():
    return UpdateCar()


@pytest.fixture()
def get_car_endpoint():
    return GetCar()


@pytest.fixture()
def delete_car_endpoint():
    return DeleteCar()


@pytest.fixture()
def new_car(create_car_endpoint, get_car_endpoint, delete_car_endpoint):
    body = {
        "name": "MuratTest",
        "data": {
            "color": "krasny",
            "size": "small"
        }
    }
    create_car_endpoint.create_new_car(body)
    create_car_endpoint.check_status_code(200)

    object_id = create_car_endpoint.json_response["id"]
    yield object_id
    get_car_endpoint.get_car(object_id)
    if get_car_endpoint.response.status_code == 200:
        delete_car_endpoint.delete_car(object_id)
        delete_car_endpoint.check_status_code(200)
