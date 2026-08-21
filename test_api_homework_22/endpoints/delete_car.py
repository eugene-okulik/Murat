import allure
import requests

from test_api_homework_22.endpoints.base_endpoint import Endpoint


class DeleteCar(Endpoint):
    @allure.step("Отправить DELETE запрос")
    def delete_car(self, object_id: int):
        self.response = requests.delete(f"{self.url}/{object_id}")
        return self.response
