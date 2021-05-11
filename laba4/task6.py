# Author: Andrii Reva, sKS-18
# Date: 11.03.2020


def task6():
    string = str(input("Input string: "))
    counter = 0
    for letter in string:
        if "а" in letter:
            counter += 1
        elif "А" in letter:
            counter += 1

    if counter >= 1:
        print("Letter 'a' has in string in counter:", counter)
    else:
        print("String hasn't letter 'a'")


task6()
