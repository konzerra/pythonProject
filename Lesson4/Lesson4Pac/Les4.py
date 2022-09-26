import os
import random
import time

from Lesson4.Lesson4Pac.InputNumber import inputNumber
from Lesson4.Lesson4Pac.InputString import inputString


def les4ex1():
    x = inputNumber('Enter number between 1-9: ')
    if x < 4:
        s = inputString('Enter string: ')
        n = inputNumber('Enter n (number of repeating: ')
        for i in range(0, n):
            print(s)
    elif 3 < x < 7:
        m = inputNumber('Enter power to raise: ')
        print(pow(x, m))
    elif 6 < x < 9:
        for i in range(0, 10):
            x = x + 1
            print(x)
    else:
        print('Error in input')


def les4ex2():
    folderPath = input("Enter folder path: ")
    filename = input("Enter filename: ")
    path = folderPath + '\\' + filename
    if os.path.exists(path):
        print('path: ' + path)
        print('size: ' + os.path.getsize(path).__str__())
        print('type: ' + os.path.splitext(path)[1])
        print("last modified: %s" % time.ctime(os.path.getmtime(path)))
        print("created: %s" % time.ctime(os.path.getctime(path)))
    else:
        print("No file found")


def les4ex3():
    answers = [
        'Nothing will happen',
        'Everything will fail',
        'Keep it up',
        'The last day is coming',
        'The president will be overthrown',
        'The boing 747 will crash at..',
        'GoPro will fail at the most interesting moment',
        'Ninebot become default'
        'Apple stock goes up',
        'Donald Trump is next president'
    ]
    x = input('Enter the question: ')
    print(answers[random.randint(0, 8)])


def les4ex4():
    x = input('Enter the string: ')
    key = input('Enter the key: ')
    words = x.split(' ')
    if key == words[0] or key == words[words.__len__() - 1]:
        for index, word in enumerate(words):
            if word == key and (index == 0 or index == words.__len__() - 1):
                print(word[::-1])
            else:
                print(word)
