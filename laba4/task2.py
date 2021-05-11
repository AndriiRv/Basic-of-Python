# Author: Andrii Reva, sKS-18
# Date: 09.03.2020

import random
from datetime import datetime


def get_random_value_from_range():
    return random.randint(3, 6)


def task2():
    print(datetime.now())

    random_value = get_random_value_from_range()
    result = ""
    result = result + str(random_value) + " "
    if random_value == 1:
        result = result + "негритенок пошел"
    elif (random_value >= 2) and (random_value <= 4):
        result = result + "негритенка пошли"
    elif (random_value >= 5) and (random_value <= 10):
        result = result + "негритят пошли"
    print(result)


task2()
