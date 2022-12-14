# Defining Function
import cmath
from numpy import log as ln


# 2.2 * x - pow(2, x)
# 11/5 - cmath.log10(x)*pow(2,x)

#x - 0.21 * cmath.sin(0.5 + x)

def f(x):
    return pow(x,2) - cmath.cos(x)


def fx(x):
    return cmath.sin(x)+(2*x)


# Implementing Secant Method

def newton(x0, e, N):
    print('\n\n*** Newton METHOD ***')
    step = 1
    condition = True
    x1 = x0
    while condition:

        x0 = x1
        x1 = x0 - (f(x0) / fx(x0))
        print('Iteration-{0}, x1 = {1} and e = {2}'.format(step, x1, abs(x1-x0)))

        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        condition = abs(x1-x0) > e
    print('\n Root is: ' + x1.__str__())


def SElab2():
    # Input Section
    x0 = float(input('Enter First Guess: '))
    e = float(input('Tolerable Error: '))
    N = int(input('Maximum Step: '))

    newton(x0,  e, N)
