# Author: Andrii Reva, sKS-18
# Date: 07.03.2020


def max_by_array_of_element(array):
    size_of_array = len(array)
    max = array[0]
    for i in range(0, size_of_array, 1):
        if max < array[i]:
            max = array[i]
    return max


def min_by_array_of_element(array):
    size_of_array = len(array)
    min = array[0]
    for i in range(0, size_of_array, 1):
        if min > array[i]:
            min = array[i]
    return min


def task5():
    n = int(input("Input count of number: "))
    array = []
    for i in range(0, n, 1):
        a = int(input("Input a: "))
        if i % 2 != 0:
            array.append(a)

    print("Max from array:", max_by_array_of_element(array))
    print("Min from array:", min_by_array_of_element(array))


task5()
