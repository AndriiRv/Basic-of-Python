# Author: Andrii Reva, sKS-18
# Date: 09.03.2020
# Andrii Reva. Spd. Interlink. SPD-UKRAINE. SPD-UKRAINE.


def task5():
    check = True
    sentences = ""

    while check:
        sentences = str(input("Input sentences: "))

        counter = 0
        for word in sentences:
            if "." in word:
                counter += 1
        if counter < 5:
            print("Your wrote", counter, "sentences, but need five. Start again.")
            check = True
        else:
            check = False

    sentences = sentences.replace(". ", ".")
    sentences = sentences.split(".")

    word_list = []

    for word in sentences:
        word_list.append(word)

    result = ""

    if word_list[len(word_list) - 2] == word_list[len(word_list) - 3]:
        for word in word_list:
            result = result + word
    else:
        result = "Fourth and Fifth sentences not the same"

    print(result)


task5()
