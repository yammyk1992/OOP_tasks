from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        """Метод для перемещения транспортного средства"""

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        """Абстрактный метод класса"""


class Bus(Transport):
    def __init__(self, model, speed):
        self._model = model
        self._speed = speed

    def go(self):
        print("bus go")

    @classmethod
    def abstract_class_method(cls):
        pass


class Model(ABC):

    @abstractmethod
    def get_pk(self):
        pass

    @staticmethod
    def get_info():
        return f"Базовый класс Model"


class ModelForm(Model):
    instance_id = 1

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = ModelForm.instance_id
        ModelForm.instance_id += 1

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
form1 = ModelForm('sdf', 'sdf')
print(form.get_pk())
print(form1.get_pk())