# Author: Andrii Reva, sKS-18
# Date: 08.03.2020


def task7():
    n = int(input("Enter the count of words: "))
    list = []
    for i in range(1, n + 1):
        word = str(input("Enter the word: "))
        list.append(word)
    index = int(input("Enter the index for word y: "))
    y = list[index - 1]
    print("List[", index, "] =", y)
    len_sum = 0
    for word in list:
        if word != y:
            len_sum += 2 * len(word)
        else:
            len_sum += len(word)
    print("Sum of length =", len_sum)
    K = 3
    print("Const K =", K)
    iterator = 0
    flag = False
    for i in range(1, int(len_sum * K), 1):
        word = list[iterator]
        if y.find(word) != -1 and int(iterator) != index - 1:
            print(word)
            flag = True
        iterator += 1
        if iterator == len(list):
            break
    if flag:
        print("Congrats!")
    else:
        print("Sorry...")


task7()
