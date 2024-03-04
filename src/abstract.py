from abc import ABC, abstractmethod


class AbcApi(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями."""
    #
    # text: str
    # per_page: int
    # page: int

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def _build_response(self):
        pass


class ManagerFile(ABC):
    """абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
     получения данных из файла по указанным критериям и удаления информации о вакансиях."""

    @abstractmethod
    def safe_file(self, file_path):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

