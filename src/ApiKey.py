from requests import request

from src.AbcClass import GetVacancy


class HeadHunterAPI(GetVacancy):
    """Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru.
    Класс уметь подключаться к API и получать вакансии."""

    __url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name_job=None, pages=None):
        """
        Получает вакансии по названию
        :param name_job: str Название вакансии
        :param pages: int Количество вакансий
        :return:
        """
        req = request('GET', self.__url, params={
            'text': name_job,
            'per_page': pages,
            'only_with_salary': True
        })
        return req.json()['items']
