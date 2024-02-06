"""Тесты с использованием pytest для модуля phone."""
import pytest

from src.phone import Phone
from config import ROOT
import os

CSV_PATH = os.path.join(ROOT, 'src', 'items.csv')


@pytest.fixture
def item_for_test():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_str(item_for_test):
    """Проверка работы магического метода __str__."""
    assert str(item_for_test) == 'iPhone 14'


def test_repr(item_for_test):
    """Проверка работы магического метода __repr__."""
    assert repr(item_for_test) == "Phone('iPhone 14', 120000, 5, 2)"


def test_name(item_for_test):
    """Проверка работы геттера."""
    assert item_for_test.number_of_sim == 2


def test_name_setter(item_for_test):
    """Проверка работы сеттера."""
    item_for_test.number_of_sim = 1
    assert item_for_test.number_of_sim == 1
    with pytest.raises(ValueError):
        item_for_test.number_of_sim = 0
