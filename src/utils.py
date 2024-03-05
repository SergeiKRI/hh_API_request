from src.ApiKey import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def user_choice_hh():
    keyword = input('Напишите название профессии: \n')
    hh_api = HeadHunterAPI()
    pages = int(input('Сколько вакансий? \n'))
    from_hh = hh_api.get_vacancies(keyword, pages)
    vacancies_list = Vacancy.cast_to_object_list(from_hh)
    print('Список вакансий с сайта "HeadHunter": \n')
    for i in vacancies_list:
        print(i)
    print('Записать, отсортированные по зарплате данные в JSON файл? \n')
    user_answer = input('Да\Нет \n').lower()
    if user_answer not in ['да']:
        print('Спасибо за использование программы')
    else:
        jsonfile_hh = JSONSaver()
        jsonfile_hh.add_vacancies(vacancies_list)
        jsonfile_hh.sort_vacancies_by_salary()
        jsonfile_hh.file_writer()
        return jsonfile_hh