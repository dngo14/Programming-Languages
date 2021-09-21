import random
import math as m
import sys
import json


def fib(n): 
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n): 
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

def main():
    print(fib2(5))
    dir(sys)
    dir(m)
    dir()
    year = 2016
    event = 'Referendum'
    print(f'Results of the {year} {event}')
    s = 'Hello, world.'
    print(str(s))
    print(repr(s))
    print(f'The value of pi is approximately {m.pi:.3f}.')
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        print(f'{name:10} ==> {phone:10d}')
    animals = 'eels'
    print(f'My hovercraft is full of {animals!r}.')
    print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print('Jack: {Jack:d}; Sjoerd: {Sjoerd}; Dcab: {Dcab}'.format(**table))
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:8d}'.format(x, x*x, x*x*x))
    print('12'.zfill(5))
    #f = open('yo.txt', 'w')
    #with open('workfile') as f:
    #    read_data = f.read()
    #f.read()
    #f.readline()
    #for line in f:
    #   print(line, end='')
    #f.write('This is a test\n')
    #x = [1, 'simple', 'list']
    #json.dumps(x)
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    # try:
    #     f = open('myfile.txt')
    #     s = f.readline()
    #     i = int(s.strip())
    # except OSError as err:
    #     print("OS error: {0}".format(err))
    # except ValueError:
    #     print("Could not convert data to an integer.")
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise
    def this_fails():
       x = 1/0
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
    raise NameError('HiThere')

    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')
    
    #with open("myfile.txt") as f:
    #for line in f:
    #    print(line, end="")


if __name__ == "__main__":
    main()
