# Defining Function
import cmath
from numpy import log as ln


# cmath.sqrt(cmath.cos(x))
# pow(2,x)/2.2


def f(x):
    return -cmath.sqrt(cmath.cos(x))


# Implementing Method

def newton(x0, e, N):
    print('\n\n*** Simple iteration METHOD ***')
    step = 1
    condition = True
    x1 = x0
    while condition:
        x0 = x1
        x1 = f(x0)
        print('Iteration-{0}, x1 = {1} and e = {2}'.format(step, x1, abs(x1 - x0)))

        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        condition = abs(x1 - x0) > e
    print('\n Root is: ' + x1.__str__())


def SElab3():
    # Input Section
    x0 = float(input('Enter First Guess: '))
    e = float(input('Tolerable Error: '))
    N = int(input('Maximum Step: '))

    newton(x0, e, N)
