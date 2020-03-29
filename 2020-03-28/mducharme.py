"""
author: mikaeld
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(c):
    return c(lambda a, b: a)


def cdr(c):
    return c(lambda a, b: b)


if __name__ == '__main__':
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
