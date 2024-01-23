"""Тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_for_test():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item_for_test):
    assert item_for_test.calculate_total_price() == 200000


def test_apply_discount(item_for_test):
    item_for_test.apply_discount()
    assert item_for_test.price * item_for_test.pay_rate == item_for_test.price