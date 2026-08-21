import allure
import requests

from test_api_homework_22.endpoints.base_endpoint import Endpoint


class UpdateCar(Endpoint):
    @allure.step("Отправить PUT запрос с новыми данными")
    def update_car(self, object_id, body):
        self.response = requests.put(f'{self.url}/{object_id}', json=body)
        self.get_json()
        return self.response
