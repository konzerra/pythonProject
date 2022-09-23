import cmath
import random


def les3ex1():
    print("Randomizing:")
    x = random.randint(1, 9)
    print("*** Random x = ", x)
    if x < 4:
        s = input('Enter string: ')
        print('Random n (number of repeating: ')
        n = random.randint(1, 10)
        print("*** Random n = ", n)
        for i in range(0, n):
            print(s)
    elif 3 < x < 7:
        print('Enter power to raise: ')
        m = random.randint(1, 5)
        print("*** Random m = ", m)
        print(pow(x, m))
    elif 6 < x < 9:
        for i in range(0, 10):
            x = x + 1
            print(x)
    else:
        print('Error in input')


def les3ex2():
    print("Randomizing:")
    x = random.randint(1, 9)
    print("*** Random x = ", x)
    if check(0, x, 4):
        s = input('Enter string: ')
        n = random.randint(1, 10)
        print("*** Random n = ", n)
        for i in range(0, n):
            print(s)
    elif check(3, x, 7):
        m = random.randint(1, 10)
        print("*** Random power = ", m)
        print(pow(x, m))
    elif check(6, x, 9):
        for i in range(0, 10):
            x = x + 1
            print(x)
    else:
        print('Error in input')


def check(a, x, b):
    return a < x < b


def les3ex3():
    x = input('enter string: ')
    for i in x.split(' '):
        print(i + ' - ' + i.__len__().__str__())
