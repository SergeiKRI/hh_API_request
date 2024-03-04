import json
import requests

#
# class FisHeadHunterAPI:
#     """Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru.
#     Класс уметь подключаться к API и получать вакансии."""
#
#     __url = 'https://api.hh.ru/vacancies'
#     # __response = None
#     #
#     # text: str = ''
#     # per_page = 10
#     # page = 20
#
#     def _sort_json_response(self):
#         self.none_in_null()
#         sorted_json = sorted(self._build_response.json()['items'], key=lambda x: x['salary']['from'], reverse=True)
#         return sorted_json
#
#     def _make_params(self):
#         params = {
#             'text': self.text,
#             'per_page': self.per_page,
#             'page': self.page,
#             'only_with_salary': True
#         }
#         return params
#
#     @property
#     def _build_response(self):
#         request_api = requests.request('GET', self.__url, params=self._make_params())
#         return request_api
#
#     def model_post_init(self) -> None:
#         HeadHunterAPI.__response = self._sort_json_response()
#         print(HeadHunterAPI.__response)
#
#     def none_in_null(self):
#         for x in self._build_response.json()['items']:
#             if x['salary']['from'] is None:
#                 x['salary']['from'] = 0
#         return
#
#     def get_vacancies(self, vacancy):
#         self.text = vacancy
#         return self.model_post_init()



class VacanciesJSON():
    def __init__(self, vacancies_list):
        """
        Создает объект класса VacanciesJSON
        """
        self.vacancies_list = vacancies_list
        # try:
        #     self.write_json(self.vacancies_params_list, VacanciesJSON.PATH)
        # except TypeError:
        #     print('Отсутсвуеют вакансии для записи в файл')

    @property
    def vacancies_params_list(self):
        """
        Возвращает параметры вакансий из списка в виде списка словарей
        :return:
        """
        vacancies_params_list = []
        for vacancy in self.vacancies_list:
            vacancies_params_list.append({
                'title': vacancy.title,
                'url': vacancy.url,
                'salary': vacancy.salary,
                'requirements': vacancy.requirements,
                'area': vacancy.area,
                'employer': vacancy.employer
            })
        return vacancies_params_list


if __name__ == '__main__':
    #     url_post = "https://httpbin.org/post"  # используемый адрес для отправки запроса
    #
    #     response = requests.post(url_post)  # отправка POST-запроса
    #
    #     print(response)  # вывод объекта класса Response
    #
    #     print(response.status_code)  # вывод статуса запроса, 200 означает, что всё хорошо
    #
    #     print(response.text)  # печать ответа в виде текста того, что вернул нам внешний сервис
    #     print(response.json())

    a = HeadHunterAPI()
    a.get_vacancies('Python')

