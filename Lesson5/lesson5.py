import string


class Lesson4ex1:
    def __init__(self, x: int, s: string, n: int, m: int):
        self.x = x
        self.s = s
        self.n = n
        self.m = m

    def run(self):
        if self.x < 4:
            for i in range(0, self.n):
                print(self.s)
        elif 3 < self.x < 7:
            print(pow(self.x, self.m))
        elif 6 < self.x < 9:
            for i in range(0, 10):
                self.x = self.x + 1
                print(self.x)
        else:
            print('Error in input')


def les5ex1():
    obj = Lesson4ex1(2, 'Some string', 3, 4)
    obj.run()


class Lesson4ex2:
    def __init__(self, m: int):
        self.m = m

    def run(self):
        print('Общество в начале XXI века')
        if 1 <= self.m < 7:
            print('Вам в детский сад')
        elif 7 <= self.m < 18:
            print('Вам в школу')
        elif 18 <= self.m < 25:
            print('Вам в профессиональное учебное заведение')
        elif 25 <= self.m < 60:
            print('Вам на работу')
        elif 60 <= self.m < 120:
            print('Вам предоставляется выбор')
        else:
            for i in range(0, 5):
                print('Ошибка! Это программа для людей!')


def les5ex2():
    obj = Lesson4ex2(2)
    obj.run()
