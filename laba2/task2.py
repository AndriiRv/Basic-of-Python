# Author: Andrii Reva, sKS-18
# Date: 07.03.2020


def task2():
    check = True
    n = 0
    while check:
        try:
            n = int(input("Input count of number: "))
            check = False
        except ValueError:
            print("\nInput int value. Try again.")
            check = True

    ak = 0
    sum_of_a = 0
    for i in range(0, n, 1):
        a = int(input("Input a: "))
        if (a % 3 == 0) and (a % 5 != 0):
            ak = ak + 1
            sum_of_a = sum_of_a + a
            print(a, "is multiple to 3 and not to 5")
        else:
            print(a, "failed by condition")
    print("\nCount of element passed by condition:", ak)
    print("Sum of element passed by condition:", sum_of_a)


task2()