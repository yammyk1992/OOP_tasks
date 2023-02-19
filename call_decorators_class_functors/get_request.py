# Необходимо объявить класс-декоратор с именем HandlerGET, который будет имитировать обработку GET-запросов на
# стороне сервера. Для этого сам класс HandlerGET нужно оформить так, чтобы его можно было применять к любой функции
# как декоратор. Например:
#
# @HandlerGET def contact(request): return "Сергей Балакирев" Здесь request - это произвольный словарь с данными
# текущего запроса, например, такой: {"method": "GET", "url": "contact.html"}. А функция должна возвращать строку.
#
# Затем, при вызове декорированной функции:
#
# res = contact({"method": "GET", "url": "contact.html"})
# должна возвращаться строка в формате:
#
# "GET: <данные из функции>"
#
# В нашем примере - это будет:
#
# "GET: Сергей Балакирев"
#
# Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если же ключ method
# принимает другое значение, например, "POST", то декорированная функция contact должна возвращать значение None.
#
# Для реализации имитации GET-запроса в классе HandlerGET следует объявить вспомогательный метод со следующей
# сигнатурой:
#
# def get(self, func, request, *args, **kwargs): ... Здесь func - ссылка на декорируемую функцию; request - словарь с
# переданными данными при вызове декорированной функции. Именно в этом методе следует формировать возвращаемую строку
# в указанном формате:
#
# "GET: Сергей Балакирев"

class HandlerGET:

    def __init__(self, func):
        self.func = func
        print(self.func)

    def __call__(self, request, *args, **kwargs):
        print(request)
        m = request.get("method", "GET")
        print(m)
        if m == "GET":
            return self.get(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f'GET:{func(request)}'


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)
