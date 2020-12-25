# Write a program to find factorial of a number.

number = int(input("Enter the number whose factorial you want :\t"))

factorial = 1

# check if the number is negative, positive or zero
if number < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       factorial *= i
   print(f"The factorial of {number} is {factorial}.")
