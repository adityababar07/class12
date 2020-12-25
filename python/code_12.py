# write a program for fabonacci series.

a = 0
b = 1
fabonacci_series = [0]

c = int(input("Enter the number of items in a fabonacci series :\t"))
for _ in range(c):
    d = a + b
    a = b
    b = d
    print(a)
    fabonacci_series.append(a)

for items in fabonacci_series:
    print(items, end=",")
print("\n")
