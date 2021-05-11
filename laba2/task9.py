# Author: Andrii Reva, sKS-18
# Date: 07.03.2020


def task9():
    count_of_head = 2000
    while count_of_head != 0:
        if count_of_head >= 33:
            count_of_head = count_of_head - 33
            print(count_of_head)
            continue
        if count_of_head >= 21:
            count_of_head = count_of_head - 21
            if count_of_head == 0:
                break
            count_of_head = count_of_head + 17
            print(count_of_head)
            continue
        if count_of_head >= 17:
            count_of_head = count_of_head - 17
            if count_of_head == 0:
                break
            count_of_head = count_of_head + 14
            print(count_of_head)
            continue
        if count_of_head >= 1:
            count_of_head = count_of_head - 1
            count_of_head = count_of_head + 349
        print(count_of_head)


task9()
