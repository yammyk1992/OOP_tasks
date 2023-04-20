CURRENT_OS = 'windows'  # 'windows', 'linux'


class WindowsFileDialog:

    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    def __init__(self, title, path, exts):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов

    def __new__(cls, *args, **kwargs):
        print(cls.__name__, "-CLS", args, "-ARGS")
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(*args)
        return cls.create_linux_filedialog(*args)

    @staticmethod
    def create_windows_filedialog(*args):
        """для создания объектов класса WindowsFileDialog;"""
        WindowsFileDialog(*args)

    @staticmethod
    def create_linux_filedialog(*args):
        """для создания объектов класса LinuxFileDialog."""
        LinuxFileDialog(*args)


dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
