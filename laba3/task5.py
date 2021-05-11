# Author: Andrii Reva, sKS-18
# Date: 08.03.2020


def task5():
    n = int(input("Enter n: "))
    right_numbers = []
    temp_numbers = []
    while True:
        question = input("Enter question: ")
        if question == "HELP":
            break
        for num in question.split():
            if int(num) <= n:
                temp_numbers = [int(num)]
        answer = input("Enter answer: ")
        if answer == "YES" and len(right_numbers) == 0:
            right_numbers = list(int(num) for num in temp_numbers)
        if answer == "YES" and len(right_numbers) > 0:
            right_numbers = list(set(right_numbers) & set(temp_numbers))
    right_numbers.sort()
    for num in right_numbers:
        if num % 3 == 0:
            print(" * ".join(str(num)))


task5()
