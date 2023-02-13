# Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:
#
# book = Book()
# book = Book(название, автор, число страниц, год издания)
# В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:
#
# title - заголовок книги (строка, по умолчанию пустая строка);
# author - автор книги (строка, по умолчанию пустая строка);
# pages - число страниц (целое число, по умолчанию 0);
# year - год издания (целое число, по умолчанию 0).
#
# Объявите в классе Book магический метод __setattr__ для проверки типов присваиваемых данных локальным свойствам
# title, author, pages и year. Если типы не соответствуют локальному атрибуту (например, title должна ссылаться на
# строку, а pages - на целое число), то генерировать исключение командой:
#
# raise TypeError("Неверный тип присваиваемых данных.")
# Создайте в программе объект book класса Book для книги:
#
# автор: Сергей Балакирев
# заголовок: Python ООП
# pages: 123
# year: 2022

class Book:

    d_types = {'title': str, 'author': str, 'pages': int, 'year': int}

    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in self.d_types and self.d_types[key] == type(value):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

        # if key == "title" and type(value) != str:
        #     raise TypeError("Неверный тип присваиваемых данных.")
        # else:
        #     object.__setattr__(self, key, value)
        #
        # if key == "author" and type(value) != str:
        #     if type(value) != int:
        #         raise TypeError("Неверный тип присваиваемых данных.")
        #     else:
        #         object.__setattr__(self, key, value)
        #
        # if key == "pages" and type(value) != int:
        #     raise TypeError("Неверный тип присваиваемых данных.")
        # else:
        #     object.__setattr__(self, key, value)
        #
        # if key == "year" and type(value) != int:
        #     raise TypeError("Неверный тип присваиваемых данных.")
        # else:
        #     object.__setattr__(self, key, value)


book = Book("Сергей Балакирев", "Python ООП", 123, 2022)
