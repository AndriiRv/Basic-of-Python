# Author: Andrii Reva, sKS-18
# Date: 07.03.2020


def task1():
    n = int(input("Input count of number: "))
    ak = 0
    for i in range(0, n, 1):
        a = int(input("Input a: "))
        if (a % 3 == 0) and (a % 5 != 0):
            ak = ak + 1
            print(a, "is multiple to 3 and not to 5")
        else:
            print(a, "failed by condition")
    print("\nCount of element passed by condition:", ak)


task1()
