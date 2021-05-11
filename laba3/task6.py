# Author: Andrii Reva, sKS-18
# Date: 08.03.2020


def task6():
    n = int(input("Enter the count of days in year: "))
    k = int(input("Enter the count of political parties: "))
    actions = set()
    for i in range(1, k + 1, 1):
        a_i = int(input("Enter a[i]: "))
        b_i = int(input("Enter b[i]: "))
        for x in range(a_i, n + 1, b_i):
            if x % 7 != 0 and x % 7 != 6:
                actions.add(x)
    print("Count of actions = ", len(actions))
    print(actions)


task6()
