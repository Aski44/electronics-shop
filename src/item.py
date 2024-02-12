import csv
import os
from abc import ABC

from config import ROOT


class InstantiateCSVError(Exception):
    """Вызывается когда файл item.csv поврежден и инициализация невозможна."""
    pass


class Item(ABC):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        """
        Возвращает текстовое представление объекта полезное для отладки
        в виде названия классов и его атрибутов.
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return self.__name

    def __add__(self, other):
        """
        Складывает количество товара в магазине.
        Проверяет, чтобы нельзя было сложить `Phone` или `Item`
        с экземплярами не `Phone` или `Item` классов.
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item или дочерние от них.')
        return self.quantity + other.quantity

    @property
    def name(self):
        """
        Геттер для чтения приватного `name`.
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Проверяет, что длина наименования товара не больше 10 символов.
        В противном случае, обрезать строку (оставить первые 10 символов).
        """
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        try:
            CSV_PATH = os.path.join(ROOT, 'src', 'items.csv')
            cls.all = []  # обнулила список
            with open(CSV_PATH, newline='', encoding="cp1251") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('_Отсутствует файл item.csv_')
        except KeyError:
            raise InstantiateCSVError('_Файл item.csv поврежден_')

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки.
        """
        float_str = float(string)
        int_numb = int(float_str)
        return int_numb

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
