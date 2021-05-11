# Author: Andrii Reva, sKS-18
# Date: 12.03.2020


def task1():
    read_text_file = open("../resources/task1.txt", "r", encoding="utf-8")
    string = ""

    count_of_words = 0
    all_count_of_letter = 0

    word_with_min_length = ""
    min_length_of_word = 0

    word_with_max_length = ""
    max_length_of_word = 0

    for line in read_text_file:
        if line == "\n":
            continue
        else:
            words_in_list = line.split(" ")

            for word_without_list in words_in_list:
                if word_without_list not in '':
                    word = word_without_list
                    all_count_of_letter += len(word)
                    if min_length_of_word == 0:
                        min_length_of_word = len(word)

                    if len(word) < min_length_of_word:
                        min_length_of_word = len(word)
                        word_with_min_length = word
                    elif len(word) > max_length_of_word:
                        max_length_of_word = len(word)
                        word_with_max_length = word

            count_of_words += len(words_in_list)
            string += line

    read_text_file.close()

    if word_with_max_length.find(",\n") or word_with_max_length.find(".\n") or word_with_max_length.find("\n"):
        word_with_max_length = word_with_max_length.replace(",\n", "")

    print(string)
    print("\nCount of words:", count_of_words)
    print("Count Of letter in words:", all_count_of_letter)
    print("Word:'", word_with_min_length, "' has the smallest length:", min_length_of_word)
    print("Word:'", word_with_max_length, "' has the biggest length:", max_length_of_word)


task1()
