class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        h = (self.clock1.hours-self.clock2.hours)
        m = (self.clock1.minutes-self.clock2.minutes)
        s = (self.clock1.seconds-self.clock2.seconds)
        if int(h) >= 0 and int(m) >= 0 and int(s) >= 0:
            return f"{h:02d}: {m:02d}: {s:02d}"
        else:
            return f"00: 00: 00"

    def __len__(self):
        difference = self.clock1.get_time() - self.clock2.get_time()
        if difference > 0:
            return difference
        else:
            return 0


class Clock:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def get_time(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds


dt = DeltaClock(Clock(0, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
str_dt = str(dt)
print(str_dt)  # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)
print(len_dt)  # разницу времен clock1 - clock2 в секундах (целое число)# 5400
print(dt)  # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
