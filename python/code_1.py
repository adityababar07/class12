# write a program to generate patterns.

no_of_rows = int(input("enter no of row you want the pattern to be followed :\t"))

for i in range(no_of_rows):
    for _ in range(i+1):
        print("*", end='')
    print()
