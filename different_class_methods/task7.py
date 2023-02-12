class SmartPhone:

    def __init__(self, model):
        self.model = model
        self.apps = []
        self.set = set()

    def add_app(self, app):
        """При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект
        соответствующего класса). """
        if type(app) not in self.set:
            # if len(list(filter(lambda x: type(x) == type(app), self.apps))) == 0:
            self.set.add(type(app))
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
