from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        """Абстрактный объект-свойство"""

    @property
    @abstractmethod
    def population(self):
        """Абстрактный объект-свойство"""

    @property
    @abstractmethod
    def square(self):
        """Абстрактный объект-свойство"""

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, *args):
        self._name = args[0]
        self._population = args[1]
        self._square = args[2]

    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f"{self._name}: {self._square}, {self._population}"


country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info())  # Россия: 354005483.0, 150000000
