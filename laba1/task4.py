# Author: Andrii Reva, sKS-18
# Date: 07.03.2020

from math import cos, sin


def numeral_f1(a, b, c, x):
    return ((a * x - b) + c) * x - b


def denominator_f1(x):
    return x - 1


def numeral_f2(x):
    return (cos(x ** 2)) ** 2 + x + 2 * sin(3 * x)


def denominator_f2():
    return -2


def task4():
    print("f1(x) = 0.5 * x - ((((a * x - b) + c) * x - b) / (x - 1))")
    print("f2(x) = ((cos * x^2)^2 + x + (2 * sin * 3 * x)) / -2")

    x = float(input("Input x: "))
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    c = float(input("Input c: "))

    result1 = 0.5 * x - (numeral_f1(a, b, c, x) / denominator_f1(x))
    result2 = numeral_f2(x) / denominator_f2()

    print("f1: ", round(result1, 2))
    print("f2: ", round(result2, 2))


task4()
