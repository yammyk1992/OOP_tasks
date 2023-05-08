from datetime import datetime


class DateError(Exception):
    pass


class DateString:
    def __init__(self, date_string):

        self.check_date(date_string)
        self.date_string = datetime.strptime(date_string, '%d.%m.%Y').strftime('%d.%m.%Y')

    def check_date(self, d):
        if len(d.split('.')) == 3:
            try:
                datetime.strptime(d, '%d.%m.%Y')
            except DateError as d:
                print(d)
        else:
            try:
                datetime.strptime(d, '%d.%m')

            except DateError as d:
                print(d)

    def __str__(self):
        return self.date_string


date = DateString("6.5.2022")
print(date)
