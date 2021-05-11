# Author: Andrii Reva, sKS-18
# Date: 07.03.2020


def task1():
    n = int(input("Input number of diapason: "))
    list = []
    for i in range(1, n + 1, 1):
        list.append(str(i))

    counter = 0
    for i in range(0, len(list), 1):
        if i == 1:
            list[i] = list[i] + "*"
            counter = counter + 1
        if "*" not in list[i]:
            if int(list[i]) % 10 == 0:
                list[i] = list[i] + "*"
                counter = counter + 1

    print("Count inserting * to list:", counter)


task1()
