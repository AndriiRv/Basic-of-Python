# Author: Andrii Reva, sKS-18
# Date: 08.03.2020

import random


def get_random_value_from_range():
    return random.randint(0, 10000)


def generator_set_of_number(set, max_elements):
    for i in range(0, max_elements, 1):
        set.add(get_random_value_from_range())
    return set


def intersection(list1, list2):
    return list1.intersection(list2)


def task3():
    max_elements = 10000

    set1 = set()
    set1_with_number = generator_set_of_number(set1, max_elements)

    set2 = set()
    set2_with_number = generator_set_of_number(set2, max_elements)

    same_elements_in_two_set = intersection(set1_with_number, set2_with_number)

    final_list = list(same_elements_in_two_set)

    final_list.sort()
    final_list.reverse()

    for i in range(0, len(final_list), 1):
        if final_list[i] % 2 == 0:
            print(final_list[i])


task3()
