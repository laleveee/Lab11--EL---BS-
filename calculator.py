# Partner 1: Eva Lalevee
# Partner 2: Brian Shultz
import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b, a)


def exp(a, b):
    return a ** b
