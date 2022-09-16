def l1ex1():
    print('Enter a:')
    a = int(input())
    print('Enter b:')
    b = int(input())
    print('Enter c:')
    c = int(input())
    res = a + b + c
    print('Sum:  ' + res.__str__())


def l1ex2():
    print('Enter b: ')
    b = int(input())
    print('Enter h: ')
    h = int(input())
    print('S: ' + ((b * h) / 2).__str__())


def l1():
    print('Enter n (pupils): ')
    n = int(input())
    print('Enter k (apples): ')
    k = int(input())
    print('everyone gets: ' + int(k / n).__str__() + ' apples')
    print('but there are: ' + (k % n).__str__() + ' apples left')


def l1ex4():
    print('Enter number: ')
    n = int(input())
    print('Next number of ' + n.__str__() + ': ' + (n + 1).__str__())
    print('Previous number of ' + n.__str__() + ': ' + (n - 1).__str__())
