# Author: Andrii Reva, sKS-18
# Date: 07.03.2020


def task7():
    n = int(input("Input n: "))
    sum = 0
    mark_value = (n * (n + 1) * ((2 * n) + 1)) / 6
    for i in range(0, n + 1, 1):
        i = i ** 2
        sum = sum + i
    print("Own sum:", sum)
    print("Mark value:", mark_value)


task7()
