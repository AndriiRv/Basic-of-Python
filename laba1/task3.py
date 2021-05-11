# Author: Andrii Reva, sKS-18
# Date: 07.03.2020


def task3():
    print("Compound interest formula: a = p * (1 + r)^n")
    print("Where: a - sum received after n years\n\t   p - sum deposited to the account\n\t   r - annual interest rate")
    print("\t   n - number of year")

    a = float(input("Input a: "))
    r = float(input("Input r (in %): "))
    n = int(input("Input n: "))
    p = a / (1 - (r / 100)) ** n

    print("Sum to be returned after", n, "year =", round(p, 2))


task3()