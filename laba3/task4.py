# Author: Andrii Reva, sKS-18
# Date: 08.03.2020


def color_in_both_cases(general_colors):
    print("Count of general colors: ", len(general_colors))
    if len(general_colors) != 0:
        print(general_colors)


def task4():
    n = int(input("Enter the count of colors for Anna: "))
    m = int(input("Enter the count of colors for Borys: "))
    anna_case = set()
    boris_case = set()
    for i in range(1, n + 1, 1):
        a = int(input("Enter the color for Anna: "))
        anna_case.add(a)
    for i in range(1, m + 1, 1):
        b = int(input("Enter the color for Borys: "))
        boris_case.add(b)
    general_colors = anna_case & boris_case
    color_in_both_cases(general_colors)

    anna_another = list(anna_case - general_colors)
    anna_another.sort()
    anna_another.reverse()
    print("Another colors in Anna's case: ", anna_another)

    boris_another = list(boris_case - general_colors)
    boris_another.sort()
    boris_another.reverse()
    print("Another colors in Boris's case: ", boris_another)


task4()
