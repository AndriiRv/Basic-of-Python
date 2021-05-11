# Author: Andrii Reva, sKS-18
# Date: 07.03.2020

from math import sqrt, log, cos


def task6():
    a = -2
    b = 2.7
    h = 0.3

    while a < b:
        y = 0
        if a <= 1:
            y = sqrt(0.8 - (0.1 * a))
        elif a > 1:
            y = 5 * log(a) + cos(a)
        print("y[", a, "] =", y)
        a = a + h


task6()
