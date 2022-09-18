# Defining Function
import cmath

#здесь твоя функция
def f(x):
    return 2.2 * x - pow(2, x)
#


# Implementing Secant Method

def secant(x0, x1, e, N):
    print('\n\n*** SECANT METHOD ***')
    step = 1
    condition = True
    x2 = 0.0
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('Iteration-{0}, x2 = {1} and e = {2}'.format(step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        condition = abs(f(x2)) > e
    print('\n Root is: ' + x2.__str__())


def SElab1():
    # Input Section
    x0 = float(input('Enter First Guess: '))
    x1 = float(input('Enter Second Guess: '))
    e = float(input('Tolerable Error: '))
    N = int(input('Maximum Step: '))

    secant(x0, x1, e, N)
