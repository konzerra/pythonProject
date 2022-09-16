import cmath


def l2ex1():
    print('Enter a:')
    a = int(input())
    print('Enter b:')
    b = int(input())
    if a > b:
        print(a)
    else:
        print(b)


def l2ex2():
    print('Enter a:')
    a = int(input())
    print('Enter b:')
    b = int(input())
    print('Enter c:')
    c = int(input())
    if a == b and a == c:
        print(3)
    else:
        if a == b or a == c or c == b:
            print(2)
        else:
            print(0)


def l2ex3():
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    # discriminant
    d = (b ** 2) - (4 * a * c)

    if d < 0:
        print('no roots')
        return
    if d == 0:
        x = (-b - cmath.sqrt(d)) / (2 * a)
        print('Only one root: {0}'.format(x))
        return
    x1 = (-b - cmath.sqrt(d)) / (2 * a)
    x2 = (-b + cmath.sqrt(d)) / (2 * a)
    print('The roots are {0} and {1}'.format(x1, x2))


def l2ex4():
    a = float(input('Enter number: '))
    if a % 100 != 0 and (a % 4 == 0 or a % 400 == 0):
        print('YES')
    else:
        print('NO')


def checkYear(x):
    if x % 10 == 1:
        return 'год'
    if 1 < x % 10 < 5:
        return 'года'
    else:
        return 'лет'


def l2ex5():
    a = int(input('Сколько вам лет: '))
    print('Вам {0} {1}'.format(a, checkYear(a)))
