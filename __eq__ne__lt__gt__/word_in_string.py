class Morph:
    def __init__(self, *args):
        self.words = [*args]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def get_word(self):
        return self.words

    def __eq__(self, other):
        return other in self.words


mw = Morph()
dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                    'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'
                    ),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'
                    ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                             )]
text = input()
count = 0
for i in text.strip(".").lower().split():
    if i in dict_words:
        count += 1
print(count)
