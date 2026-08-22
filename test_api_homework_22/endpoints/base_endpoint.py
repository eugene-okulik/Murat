import allure
import requests


class Endpoint():
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json_response = None

    @allure.step("Проверяем статус код")
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code, (f'Ожидаемый статус кода {status_code}, '
                                                          f'получен {self.response.status_code}')

    # Получает Жсон из ответа
    def get_json(self):
        try:
            self.json_response = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json_response = None

    @allure.step("Проверить данные ответа")
    def check_response_data(self, body):
        assert self.json_response["name"] == body["name"]
        assert self.json_response["data"]["color"] == body["data"]["color"]
