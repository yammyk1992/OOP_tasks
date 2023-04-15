class VideoRating:
    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rate):
        if rate not in range(0, 6):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = rate


class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title  # заголовок видео (строка)
        self.descr = descr  # описание видео (строка)
        self.path = path  # путь к видеофайлу
        self.rating = VideoRating()


v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating)  # 0
v.rating.rating = 5
print(v.rating.rating)  # 5
title = v.title
print(title, "TITLE")
descr = v.descr
print(descr, "DESCR")
# v.rating.rating = 6  # ValueError
