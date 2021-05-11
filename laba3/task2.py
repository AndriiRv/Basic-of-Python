# Author: Andrii Reva, sKS-18
# Date: 08.03.2020

import random


def get_random_value_from_range(range):
    return random.randint(0, range)


def generator_list_of_number(n, list, max_elements):
    for i in range(0, max_elements, 1):
        list.append(get_random_value_from_range(n))
    return list


def intersection(lst1, lst2):
    return [value for value in lst1 if value in lst2]


def task2():
    n = int(input("Input number of diapason: "))
    max_elements = 100000

    list1 = []
    list1_with_number = generator_list_of_number(n, list1, max_elements)

    list2 = []
    list2_with_number = generator_list_of_number(n, list2, max_elements)

    same_elements_list = intersection(list1_with_number, list2_with_number)
    counter = 0
    for i in range(0, len(same_elements_list), 1):
        if same_elements_list[i] != 0:
            if (same_elements_list[i] % 1 == 0) and (same_elements_list[i] % same_elements_list[i] == 0):
                counter = counter + 1

    print("Count of number:", counter)


task2()
