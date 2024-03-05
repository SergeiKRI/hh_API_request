class Vacancy:
    """
    Информация о вакансии
    """
    def __init__(self, vacancy_title=None, town=None, salary_from=0, salary_to=0, employment=None, url=None):
        self.vacancy_title: str = vacancy_title
        self.town: str = town
        self.salary_from: int = salary_from
        self.salary_to: int = salary_to
        self.employment: str = employment
        self.url: str = url

    def __str__(self):
        return f'название вакансии: {self.vacancy_title}\n' \
               f'город: {self.town}\n' \
               f'зарплата от: {self.salary_from}\n' \
               f'зарплата до: {self.salary_to}\n' \
               f'тип занятости: {self.employment}\n' \
               f'ссылка на вакансию: {self.url}\n'

    def __repr__(self):
        return self.vacancy_title

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Вакансию можно сравнивать только с вакансией')
        return self.salary_from < other.salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Вакансию можно сравнивать только с вакансией')
        return self.salary_from > other.salary_from


    @staticmethod
    def cast_to_object_list(hh_vacancies):
        """
        создает список экземпляров
        :return:
        """
        hh_list =[]
        for v in hh_vacancies:
            hh_title = v['name']
            if not (v['area']) is None:
                hh_town = v['area']['name']
            else:
                hh_town = None
            if not ((v['salary'] is None) or v['salary']['from'] is None):
                salary_from = v['salary']['from']
                salary_to = v['salary']['to']
            elif not ((v['salary'] is None) or v['salary']['to'] is None):
                salary_from = 0
                salary_to = v['salary']['to']
            else:
                salary_from = 0
                salary_to = 0
            hh_employment = v['employment']['name']
            hh_url = v['alternate_url']
            hh_vacancy = Vacancy(hh_title, hh_town, salary_from, salary_to, hh_employment, hh_url)
            hh_list.append(hh_vacancy)
        return hh_list

    def to_dict(self):
        """
        Возвращает вакансию в виде словаря
        """
        return {
            'vacancy_title': self.vacancy_title,
            'town': self.town,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'employment': self.employment,
            'url': self.url
        }

    @staticmethod
    def from_dict(vacancy_dict):
        """
        Возвращает вакансию в виде списка
        """
        return Vacancy(
            vacancy_dict['vacancy_title'],
            vacancy_dict['town'],
            vacancy_dict['salary_from'],
            vacancy_dict['salary_to'],
            vacancy_dict['employment'],
            vacancy_dict['url']
        )


class Vacancies:
    """ Обработка списка вакансий"""

    __all_vacancies = []

    # def __add__(self, other):
    #     return self.__all_vacancies.append(other)

    def __repr__(self):
        return self.all_vacancies

    def add_vacancies(self, new_vacancies):
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        self.__all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        a = []
        for i in self.__all_vacancies:
            a.append(i.to_dict())
        return a