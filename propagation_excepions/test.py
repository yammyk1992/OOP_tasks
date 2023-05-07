from abc import abstractmethod


class Test:
    def __init__(self, descr):
        if not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

        self.descr = descr

    @abstractmethod
    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)

        if type(ans_digit) not in (int, float):
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit = ans_digit

        if type(max_error_digit) not in (int, float) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans)  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
try:
    test_ans_digit = TestAnsDigit(descr, ans)
    res = test_ans_digit.run()
    print(res)

except ValueError as v:
    print(v)
