"""Тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from config import ROOT
import os

CSV_PATH = os.path.join(ROOT, 'src', 'items.csv')

@pytest.fixture
def item_for_test():
    return Item("Смартфон", 10000, 20)

# @pytest.fixture
# def csv_for_test():
#     return

def test_name(item_for_test):
    assert item_for_test.name == 'Смартфон'

def test_name_setter(item_for_test):
    item_for_test.name = 'СуперСмартфон'
    assert item_for_test.name == 'СуперСмарт'

def test_instantiate_from_csv(item_for_test):
    item_for_test.instantiate_from_csv(CSV_PATH)  # создание объектов из данных файла
    assert len(Item.all) == 5
    item = item_for_test.all[0]
    assert item.name == 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_calculate_total_price(item_for_test):
    assert item_for_test.calculate_total_price() == 200000


def test_apply_discount(item_for_test):
    item_for_test.apply_discount()
    assert item_for_test.price * item_for_test.pay_rate == item_for_test.price