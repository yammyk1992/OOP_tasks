class Note:
    available_values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in self.available_values:
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')

        object.__setattr__(self, key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    available_values = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    instance = None

    def __init__(self):
        for k, v in zip(self.__slots__, self.available_values):
            setattr(self, k, Note(v, 0))

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __getitem__(self, item):
        """Вызывается когда нужно получить значение из списка напрямую в объекте, в item прилетает индекс"""
        if not (0 <= item < 7):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[item])


notes = Notes()
nota = notes[2]  # ссылка на ноту ми
print(nota)
notes[3]._ton = -1  # изменение тональности ноты фа
print(notes[-1])
