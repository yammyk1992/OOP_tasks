class Lib:
    def __init__(self):
        self.book_list = []

    def __str__(self):
        return f"{self.book_list}"

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            self.book_list.pop(other)
            return self

        self.book_list.remove(other)
        return self

    def __isub__(self, other):
        if isinstance(other, int):
            self.book_list.pop(other)
            return self
        self.book_list.remove(other)
        return self


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


lib = Lib()
book = Book("title", "author", 1992)

lib = lib + book  # добавление новой книги в библиотеку

lib += book

lib = lib - book  # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)

lib -= book

lib = lib - 4  # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
# lib -= indx

n = len(lib)  # n - число книг
print(n)
