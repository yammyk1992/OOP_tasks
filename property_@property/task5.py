class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) == int and 9999 >= w > 0:
            if self.__width != w:
                self.__width = w
                self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) == int and 9999 >= h > 0:
            if self.__height != h:
                self.__height = h
                self.show()


a = WindowDlg("АЛё", 25, 25)

a.width = 56
