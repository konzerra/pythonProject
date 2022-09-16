import cmath


def l3ex1():
    a = float(input('Enter a: '))
    print(int(a % 10))


def l3ex2():
    a = float(input('Enter a: '))
    print(a % 1)


def l3ex3():
    n = int(input('Enter number: '))
    print(n // 10 % 10)


def l3ex4():
    a = int(input('Enter a: '))
    b = a // 100
    c = (a // 10) % 10
    d = a % 10
    print(b + c + d)


def l3ex5():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    print('hypotenuse: ' + cmath.sqrt(pow(a, 2) + pow(b, 2)).__str__())


def l3ex6():
    n = int(input('Enter number: '))
    print('{0} - thousands'.format(n // 1000))
    print('{0} - hundreds'.format((n // 100) % 10))
    print('{0} - tens '.format((n // 10) % 10))
    print('{0} - ones '.format(n % 10))
