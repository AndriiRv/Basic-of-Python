# Author: Andrii Reva, sKS-18
# Date: 07.03.2020
from math import pi


def task1():
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))

    cone_volume = 1 / 3 * pi * radius * 2 * height
    cylinder_volume = pi * radius ** 2 * height
    sphere_volume = 3 / 4 * pi * radius ** 3

    print("The volume of a cone: ", cone_volume)
    print("The volume of a cylinder: ", cylinder_volume)
    print("The volume of a sphere: ", sphere_volume)


task1()
