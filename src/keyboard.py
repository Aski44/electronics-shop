from src.item import Item


class MixinLang:
    """Класс-миксин для товара 'клавиатура'."""

    LANG = ['EN', 'RU']

    def __init__(self):
        self.__language = self.LANG[0]

    @property
    def language(self):
        """Геттер для чтения приватного 'language'."""
        return self.__language

    def change_lang(self):
        """Метод для изменения языка (раскладки клавиатуры)."""
        if self.language == self.LANG[0]:
            self.__language = self.LANG[1]
        else:
            self.__language = self.LANG[0]
        return self.language


class Keyboard(Item, MixinLang):
    """Класс для товара 'клавиатура'."""

    def __init__(self, name: str, price: float, quantity: int):
        """
        Расширяет функционал класса 'Item'.
        Добавляет дополнительный атрибут 'language'.
        """
        super().__init__(name, price, quantity)
        self.__language = "EN"