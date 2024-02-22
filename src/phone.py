from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Расширяет функционал класса Item.
        Добавляет дополнительный атрибут, содержащий количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Геттер для для чтения приватного number_of_sim."""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_value):
        """
        Сеттер для атрибута number_of_sim.
        Проверяет, что значение number_of_sim целое число больше нуля.
        В противном случае, выкидывает ошибку ValueError.
        """
        if isinstance(new_value, int) and new_value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = int(new_value)

    def __repr__(self):
        """
        Возвращает текстовое представление объекта полезное для отладки
        в виде названия класса и его атрибутов.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
