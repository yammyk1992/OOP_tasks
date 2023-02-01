class Car:
    def __init__(self, model=''):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, m):
        if type(m) == str and 100 > len(m) > 2:
            self.__model = m


car = Car()
car.model = "BM"
print(car.__dict__)
