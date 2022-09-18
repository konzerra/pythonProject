def les2ex1():
    s = input('Enter string: ')
    print(max(s.split(' '), key=len))


def les2ex2():
    s = input('Enter string: ')
    print(max(s.split(';'), key=len))


def les2ex3():
    s = input('Enter string: ')
    m = input('Enter character: ')
    minstr = min(s.split(' '), key=len)
    index = s.index(minstr)
    print(s[:index]+m+s[index:])


def les2ex4():
    s = input('Input text: ')
    syntax = input('Input syntax: ')
    if syntax in s.split(' '):
        print('Found!')
    else:
        print('Not found!')


def les2ex5():
    s = input('Enter string: ')
    m = input('Enter character: ')
    print(s.split(m).__len__())



