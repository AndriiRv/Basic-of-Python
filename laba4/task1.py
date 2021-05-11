# Author: Andrii Reva, sKS-18
# Date: 09.03.2020
# Andrii reva. SPD-ukraine. CHNU.
from datetime import datetime


def task1():
    print(datetime.now())

    string = input("Input text: ")
    string = string.replace(". ", ".")
    sentences_list = string.split(".")
    for sentence in sentences_list:
        if sentence == "":
            continue
        words_in_sentence = sentence.split(" ")
        count_of_words = len(words_in_sentence)
        print("Count of words in -", sentence, ":", count_of_words)

    count_of_sentences = len(sentences_list) - 1
    print("Count of sentences:", count_of_sentences)


task1()
