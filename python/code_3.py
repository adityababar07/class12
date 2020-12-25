# Write a program that recieves 4 digit no. and calculate sum of squares of first 2 digits and last 2 digits. 

import math

def sum_of_squares(number):

    x = int(number[0:2])
    y = int(number[2:5])
    z = math.pow(x, 2)+ math.pow(y, 2)
    print(f"the sum of the square of the two numbers is {z}.")

number = input("enter a four digit number:\t")

sum_of_squares(number)

