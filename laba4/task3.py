# Author: Andrii Reva, sKS-18
# Date: 09.03.2020

import random
from datetime import datetime


def get_random_value_from_range(length_of_list):
    return random.randint(0, length_of_list)


def task3():
    print(datetime.now())

    science = ["The cars can be fly!", "An androids conquered the world!",
               "Do you know, when you sleep, you only wasted a time?"]

    random_value = get_random_value_from_range(len(science) - 1)

    began_phrase = str(input("Input began phrase: "))

    result = ""
    result = result + began_phrase + " " + science[random_value]

    print(result)


task3()
