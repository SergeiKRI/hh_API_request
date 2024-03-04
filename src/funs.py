from abc import ABC

import requests


# from src.abstract import AbcApi


class HeadHunterAPI:
    """Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru.
    Класс уметь подключаться к API и получать вакансии."""

    __url = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.request_api = requests.request('GET', self.__url, params={
            'per_page': 10,
            'page': 20,
            'only_with_salary': True
        })

        self.title = None
        self.salary_from = self.request_api.json()['items'][0]['salary']['from']
        self.salary_to = self.request_api.json()['items'][0]['salary']['to']

    def __lt__(self, other):
        """метод для сравнения размера зарплаты"""

        if self.salary_to == 'None' and self.salary_from != 'None':
            return

    def get_vacancies(self):
        pass

    def _build_response(self):
        pass


if __name__ == '__main__':
    a = HeadHunterAPI()
    print(type(a.salary_to))
