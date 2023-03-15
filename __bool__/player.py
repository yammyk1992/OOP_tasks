class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __len__(self):
        return self.score > 0

    def __bool__(self):
        return int(self.score) > 0


lst_in = ['Балакирев; 34; 2048',
          'Mediel; 27; 0',
          'Влад; 18; 9012',
          'Nina P; 33; 0']

players = [Player(*lst_in[i].split(";")) for i in range(len(lst_in))]
players_filtered = list(filter(lambda x: bool(x), players))
print(players_filtered)
