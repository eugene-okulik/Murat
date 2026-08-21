import requests
import allure

from test_api_homework_22.endpoints.base_endpoint import Endpoint


class CreateCar(Endpoint):
    @allure.step("оТПРАВЛЯЕТ POST запрос на создание объекта")
    def create_new_car(self, body):
        self.response = requests.post(
            self.url,
            json=body
        )

        self.get_json()

        return self.response
