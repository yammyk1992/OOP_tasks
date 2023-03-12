lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_bs = []
for i in lst_in:
    args = list(map(str.strip, i.split(";")))
    args[-1] = int(args[-1])
    lst_bs.append(BookStudy(*args))
# unique_books = 0
# for y in lst_bs:
#     if hash(y) == hash(y):
#         unique_books += 1
# print(unique_books)
unique_books = len(set(hash((i.name, i.author)) for i in lst_bs))
print(unique_books)
