class Server:
    server_ip = 1

    def __init__(self):
        self.buffer = []
        self.ip = Server.server_ip
        Server.server_ip += 1
        self.router = None

    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
        (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);"""
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает
         входной буфер;"""
        b = self.buffer[:]
        self.buffer.clear()
        return b

    def get_ip(self):
        """возвращает свой IP-адрес."""
        return self.ip


class Router:

    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру (для простоты, каждый сервер соединен
        только с одним роутером); """
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера;"""
        s = self.servers.pop(server.ip, False)
        if s:
            s.router = None

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам (после
        отправки буфер должен очищаться). """
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers[d.ip].buffer.append(d)
        self.buffer.clear()


class Data:

    def __init__(self, text, ip):
        self.data = text
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
print(router.link(sv_to))
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
print(router.send_data())
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
