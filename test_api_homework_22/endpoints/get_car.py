import allure
import requests

from test_api_homework_22.endpoints.base_endpoint import Endpoint


class GetCar(Endpoint):
    @allure.step("Получает объект")
    def get_car(self, object_id: int):
        self.response = requests.get(f"{self.url}/{object_id}")
        self.get_json()
        return self.response

    @allure.step("Проверить ID полученного объекта")
    def check_object_id(self, object_id):
        assert self.json_response["id"] == object_id
