"""Тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone
from config import ROOT
import os

CSV_PATH = os.path.join(ROOT, 'src', 'items.csv')


@pytest.fixture
def item_for_test():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item_for_test_2():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(item_for_test):
    """Проверка работы магического метода __repr__."""
    assert repr(item_for_test) == "Item('Смартфон', 10000, 20)"


def test_str(item_for_test):
    """Проверка работы магического метода __str__."""
    assert str(item_for_test) == 'Смартфон'


def test_add(item_for_test, item_for_test_2):
    """Проверка работы магического метода __add__."""
    assert item_for_test_2 + item_for_test == 25
    assert item_for_test_2 + item_for_test_2 == 10
    with pytest.raises(ValueError):
        item_for_test_2 + 5


def test_name(item_for_test):
    """Проверка работы геттера."""
    assert item_for_test.name == 'Смартфон'


def test_name_setter(item_for_test):
    """Проверка работы сеттера."""
    item_for_test.name = 'СуперСмартфон'
    assert item_for_test.name == 'СуперСмарт'


def test_instantiate_from_csv(item_for_test):
    """Проверка создания объектов из данных файла"""
    item_for_test.instantiate_from_csv()
    assert len(Item.all) == 5
    item = item_for_test.all[0]
    assert item.name == 'Смартфон'


def test_string_to_number():
    """Проверка метода, возвращающего число из числа-строки."""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_calculate_total_price(item_for_test):
    """Проверка расчета общей стоимости конкретного товара в магазине."""
    assert item_for_test.calculate_total_price() == 200000


def test_apply_discount(item_for_test):
    """Проверка применения установленной скидки для конкретного товара."""
    item_for_test.apply_discount()
    assert item_for_test.price * item_for_test.pay_rate == item_for_test.price


def test_FileNotFoundError(item_for_test):
    """Проверка отлавливания ошибки (если файл отсутствует)."""
    with pytest.raises(FileNotFoundError, match='_Отсутствует файл item.csv_'):
        item_for_test.instantiate_from_csv()


def test_InstantiateCSVError(item_for_test):
    """Проверка отлавливания ошибки (если файл поврежден)."""
    with pytest.raises(InstantiateCSVError, match='_Файл item.csv поврежден_'):
        item_for_test.instantiate_from_csv()
