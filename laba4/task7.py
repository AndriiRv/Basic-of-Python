# Author: Andrii Reva, sKS-18
# Date: 11.03.2020


def one_char(string_number, length):
    print(string_number[length - 1], "од.")


def two_char(string_number, length):
    print(string_number[length - 2], "дес.", string_number[length - 1], "од.")


def three_char(string_number, length):
    print(string_number[length - 3], "сот.", string_number[length - 2], "дес.", string_number[length - 1], "од.")


def fourth_char(string_number, length):
    print(string_number[length - 4], "тис.", string_number[length - 3], "сот.", string_number[length - 2], "дес.",
          string_number[length - 1], "од.")


def task7():
    string_number = str(input("Input string number: "))
    length = len(string_number)

    if length == 1:
        one_char(string_number, length)
    elif length == 2:
        two_char(string_number, length)
    elif length == 3:
        three_char(string_number, length)
    elif length == 4:
        fourth_char(string_number, length)


task7()
