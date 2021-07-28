class Items:
    def __init__(self):
        self._url = None
        self._title = None
        self._price = None
        self._img = None
        self._collected_date = None

    @property
    def url(self):
        return self._url

    @property
    def title(self):
        return self._title

    @property
    def price(self):
        return self._price

    @property
    def img(self):
        return self._img

    @property
    def collected_date(self):
        return self._collected_date

    @url.setter
    def url(self, value):
        self._url = value

    @title.setter
    def title(self, value):
        self._title = value

    @price.setter
    def price(self, value):
        self._price = value

    @img.setter
    def img(self, value):
        self._img = value

    @collected_date.setter
    def collected_date(self, value):
        self._collected_date = value


