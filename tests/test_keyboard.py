"""Тесты с использованием pytest для модуля keyboard."""
import pytest

from src.keyboard import Keyboard


@pytest.fixture
def item_for_test():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(item_for_test):
    """Проверка работы магического метода __str__."""
    assert str(item_for_test) == "Dark Project KD87A"


def test_language(item_for_test):
    """Проверка работы геттера."""
    assert str(item_for_test.language) == "EN"


def test_change_lang(item_for_test):
    """Проверка работы метода миксины изменения языка."""
    assert item_for_test.change_lang() == "RU"
    assert item_for_test.change_lang() == "EN"

