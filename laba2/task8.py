# Author: Andrii Reva, sKS-18
# Date: 07.03.2020

from math import pi


def task8():
    epsilon = 10 ** -5
    st = (pi ** 2) / 12
    number = 1
    i = pow(number, -2)
    sum = i
    counter = 0
    while abs(i) < epsilon:
        if counter % 2 != 0:
            counter += 1
            sum += i
            number += 1
        else:
            counter += 1
            sum -= i
            number -= 1
        i = number ** -2
    print("Sum:", sum)
    print("St:", st)


task8()
