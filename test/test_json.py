import json
import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def v():
    v = Vacancy("Ведущий програмист-разработчик Unity, C#",
                "Москва",
                120000,
                250000,
                "Полная занятость",
                "https://hh.ru/vacancy/93159478")
    v1 = Vacancy("Помощник Депутата (по работе в Госдуме)",
                 "Москва",
                 70000,
                 0,
                 "Полная занятость",
                 "https://hh.ru/vacancy/92886819")
    list_v = [v, v1]

    return list_v


def test_file_writer(v):
    pass
