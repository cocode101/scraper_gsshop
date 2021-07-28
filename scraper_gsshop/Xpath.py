class Xpath:
    def __init__(self):
        self._title = None
        self._price = None
        self._img = None

    @property
    def title(self):
        return self._title

    @property
    def price(self):
        return self._price

    @property
    def img(self):
        return self._img

    @title.setter
    def title(self, value):
        self._title = value

    @price.setter
    def price(self, value):
        self._price = value

    @img.setter
    def img(self, value):
        self._img = value
