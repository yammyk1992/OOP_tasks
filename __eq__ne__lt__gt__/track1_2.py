class Track:
    """класс Track (маршрут)"""

    def __init__(self, start_x, start_y):
        self.tracks = []
        self.start_x = start_x
        self.start_y = start_y

    def add_track(self, tr):
        self.tracks.append(tr)

    def get_tracks(self):
        return tuple(self.tracks)

    def __len__(self):
        len_1 = ((self.start_x - self.tracks[0].x) ** 2 + (self.start_x - self.tracks[0].y) ** 2) ** 0.5
        return int(len_1 + sum(self.__get_lenght(i) for i in range(1, len(self.tracks))))

    def __get_lenght(self, i):
        return ((self.tracks[i-1].x - self.tracks[i].x) ** 2 + (self.tracks[i-1].y - self.tracks[i].y) ** 2) ** 0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


class TrackLine:
    """Каждый линейный сегмент маршрута определяется классом TrackLine"""

    def __init__(self, to_x, to_y, max_speed):
        self._to_x = to_x
        self._to_y = to_y
        self._max_speed = max_speed

    @property
    def x(self):
        return self._to_x

    @property
    def y(self):
        return self._to_y

    @property
    def max_speed(self):
        return self.max_speed


track1 = Track(0, 0)
track2 = Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
# print(len(track1))
res_eq = track1 == track2  # маршруты равны, если равны их длины
# track1 != track2  # маршруты не равны, если не равны их длины
# track1 > track2  # True, если длина пути для track1 больше, чем для track2
# track1 < track2  # True, если длина пути для track1 меньше, чем для track2
