# Author: Andrii Reva, sKS-18
# Date: 11.03.2020


def task8():
    string = str(input("Input string: "))

    for letter in string:
        char_number = ord(letter)
        char_number = char_number + 5
        print(chr(char_number), end='')


task8()
