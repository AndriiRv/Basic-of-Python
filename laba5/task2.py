# Author: Andrii Reva, sKS-18
# Date: 12.03.2020

import numpy as np
from numpy.random.mtrand import randint


def task2():
    n = int(input("Size arrays: "))
    a = np.array([randint(1, 100) for i in range(0, n, 1)], int)
    b = np.array([randint(1, 100) for i in range(0, n, 1)], int)
    print("First array:", a)
    print("Second array:", b)
    c = a * b
    print("Third array: ", c)


task2()