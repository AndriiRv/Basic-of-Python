# Author: Andrii Reva, sKS-18
# Date: 12.03.2020

import numpy as np


def task3():
    array = np.array([i for i in range(1, 196, 1)], int)

    array_with_filtered_values = []
    for i in range(0, len(array), 1):
        if array[i] % 3 == 0:
            array_with_filtered_values.append(array[i])

    new_array = np.array([array_with_filtered_values], int)

    print("Array:")
    print(new_array)


task3()
