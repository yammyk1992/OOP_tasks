filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2"
                                                                                                               ".xls"]


class FileAcceptor:
    def __init__(self, *args):
        self.s = args

    def __str__(self):
        return f'{self.s}'

    def __call__(self, name, *args, **kwargs):
        return True if name.split(".")[-1] in self.s else False

    def __add__(self, other):
        """для добавления. other - значение справа"""
        return FileAcceptor(*(self.s + other.s))


acceptor = FileAcceptor(('jpg', 'bmp', 'jpeg'))
# передаём в фильтер коллекцию filenames!
image_filenames = filter(acceptor, filenames)

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")
print(acceptor12)
