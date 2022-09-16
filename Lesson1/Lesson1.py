import cmath


def les1ex1():
    x = int(input('Enter number between 1-9: '))
    if x < 4:
        s = input('Enter string: ')
        n = int(input('Enter n (number of repeating: '))
        for i in range(0, n):
            print(s)
    elif 3 < x < 7:
        m = int(input('Enter power to raise: '))
        print(pow(x, m))
    elif 6 < x < 9:
        for i in range(0, 10):
            x = x + 1
            print(x)
    else:
        print('Error in input')


def les1ex2():
    print('Общество в начале XXI века')
    m = int(input('Введите ваш возраст: '))

    if 1 <= m < 7:
        print('Вам в детский сад')
    elif 7 <= m < 18:
        print('Вам в школу')
    elif 18 <= m < 25:
        print('Вам в профессиональное учебное заведение')
    elif 25 <= m < 60:
        print('Вам на работу')
    elif 60 <= m < 120:
        print('Вам предоставляется выбор')
    else:
        for i in range(0, 5):
            print('Ошибка! Это программа для людей!')
