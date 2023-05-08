class ConnectionError(Exception):
    pass


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = False
        # self.login = input()
        # self.password = input()

    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.close()
        return False
