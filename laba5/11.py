# Author: Andrii Reva, sKS-18
# Date: 12.03.2020


def task1(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str

print(task1("Array"))

# task1()
