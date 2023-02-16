filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]


class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, name, *args, **kwargs):
        # start = name.rfind(".")
        # lst = "" if start == -1 else name[start + 1:]
        # return lst in self.extensions
        return name.split(".")[-1] in self.extensions


acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# передаём в фильтер коллекцию filenames!
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
