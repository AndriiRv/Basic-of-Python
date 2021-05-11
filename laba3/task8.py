# Author: Andrii Reva, sKS-18
# Date: 08.03.2020


def task8():
    stack = [["Big Avarat", 4365],
             ["Demavend", 5610],
             ["Mauna-Kea", 4205],
             ["Everest", 8848],
             ["Vinson Massif", 4892]
             ]

    for i in range(0, len(stack)):
        print(stack[i])

    n = int(input("Enter count first elements which will be remove from stack: "))
    for i in range(0, n):
        stack.pop(0)

    avg = 0
    print("All mountains: ")
    for key, value in stack:
        avg = avg + value
    avg = avg / len(stack)
    print("Average height mountains:", avg)


task8()
