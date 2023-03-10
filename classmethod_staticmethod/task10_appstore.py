class AppStore:
    lst = []

    def add_application(self, app):
        self.lst.append(app)

    def remove_application(self, app):
        if app in self.lst:
            self.lst.remove(app)

    def block_application(self, app):
        if app in self.lst:
            app.blocked = True

    def total_apps(self):
        return len(self.lst)


class Application:

    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.block_application(app_youtube)
store.remove_application(app_youtube)
app_j = Application("JJJ")
store.add_application(app_j)
store.remove_application(app_j)
print(store.total_apps())


