class Viber:
    lst = []

    @classmethod
    def add_message(cls, msg):
        """добавление нового сообщения в список сообщений;
        """
        return cls.lst.append(msg)

    @classmethod
    def remove_message(cls, msg):
        """удаление сообщения из списка;
        """
        return cls.lst.remove(msg)

    @classmethod
    def set_like(cls, msg):
        """поставить/убрать лайк для сообщения msg
        (если лайка нет то он ставится, если уже есть, то убирается);
        """
        if msg in cls.lst and msg.fl_like == True:
            msg.fl_like = False
            return msg.fl_like
        else:
            msg.fl_like = True
            return msg.fl_like

    @classmethod
    def show_last_message(cls, x):
        """отображение последних сообщений;
        """
        return reversed(cls.lst[:x])

    @staticmethod
    def total_messages():
        """звращает общее число сообщений.
        """
        return len(Viber.lst)


class Message:
    """позволяет создавать объекты-сообщения со следующим
    набором локальных свойств:
    text - текст сообщения (строка);
    fl_like - поставлен или не поставлен лайк у сообщения
    (булево значение True - если лайк есть и False - в противном
    случае, изначально False);
    P.S. Как хранить список сообщений, решите самостоятельно.
    """

    def __init__(self, text):
        self.text = text
        self.fl_like = False


msg = Message("Всем привет!")

Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
print(Viber.set_like(msg))
print(Viber.set_like(msg))
print(Viber.set_like(msg))

Viber.remove_message(msg)
