# Author: Andrii Reva, sKS-18
# Date: 09.03.2020


def task4():
    words = str(input("Input words through spacebar: "))
    words = words.split(" ")

    word_list = []

    for word in words:
        word_list.append(word)

    word_list.sort()

    print(word_list)


task4()
