# Author: Andrii Reva, sKS-18
# Date: 07.03.2020


def task4():
    sum_fa = 0
    n = int(input("Input count of number: "))
    for i in range(0, n, 1):
        a = int(input("Input a: "))
        if a % 2 == 0:
            fa = a ** (2 * a)
        elif a % 2 == 1:
            fa = 3 * a
        else:
            fa = a
        sum_fa = sum_fa + fa
    print("Sum fa:", sum_fa)


task4()
