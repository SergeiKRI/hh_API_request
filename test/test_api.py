from abc import ABC
from src.AbcClass import GetVacancy
from src.ApiKey import HeadHunterAPI


def test_issubclass():
    assert issubclass(GetVacancy, ABC)
    assert issubclass(HeadHunterAPI, GetVacancy)