# write a program to find the area of a regular polygon.

from math import tan, pi

no_sides = int(input("enter the number of sides in your regular polygon :\t"))

length = int(input("enter the length of a side:\t"))

a = (length**2)*no_sides/(4 * tan(pi/no_sides))

print(f"the area of the regular polygon is {a} ")
