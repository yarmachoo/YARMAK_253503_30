class Person:
    def __init__(self, full_name, birth_date, birth_month, birth_year):
        """Initializer of class"""
        self._full_name = full_name
        self._birth_date = birth_date
        self._birth_month = birth_month
        self._birth_year = birth_year

    @property
    def name(self):
        """Getter of name"""
        return self._full_name

    @name.setter
    def name(self, full_name):
        """Setter of name"""
        self._full_name = full_name

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @property
    def birth_month(self):
        return self._birth_month

    @birth_month.setter
    def birth_month(self, birth_month):
        self._birth_month = birth_month

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, birth_year):
        self._birth_year = birth_year

    def __str__(self):
        return f"{self._full_name}, {self._birth_date}.{self._birth_month}.{self._birth_year}"
