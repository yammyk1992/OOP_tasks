stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]


class StringText:
    def __init__(self, string):
        self.string = list(string)

    def __len__(self):
        return len(self.string)

    def validate(self):
        return list(map(lambda x: list(map(lambda w: w.strip("-?!,.;") if w != '–' else w, x.split())), self.string))

    def __gt__(self, other):
        return len(self.validate()) > len(other.validate())

    def __ge__(self, other):
        return len(self) >= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


strip_chars = "–?!,.;"
lst_text = [StringText(x.strip(strip_chars) for x in line.split() if len(x.strip(strip_chars)) > 0) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [" ".join(x.string) for x in lst_text_sorted]
print(lst_text_sorted)
