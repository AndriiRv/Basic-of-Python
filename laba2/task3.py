# Author: Andrii Reva, sKS-18
# Date: 07.03.2020


def task3():
    sum_of_formula = 0
    for i in range(0, 30, 1):
        if i % 2 != 0:
            ai = i + ((10 * i) ** 2)
            bi = (i ** 2) / 7
        else:
            ai = 2 * i
            bi = i ** 5
        sum_of_formula = sum_of_formula + ((ai - bi) ** 2)

    print("Sum:", sum_of_formula)


task3()
