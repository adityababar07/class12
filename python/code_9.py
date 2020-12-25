# write a program to add a element at end of a list only if element is not in list.

a = [1, 7, 5, 25, 78, 38]

while True:
    try:
        input0 = int(input("Enter a number between 0-100 :\t"))
    except:
        print("Invalid entery")

    if input0 in a:
        print("The element you want to enter already exists in the list. Try again!!")
    else:
        a.append(input0)
        print(a)
        decision = input("Do you want to countinue ? | ('y','n') :\t")
        if decision == 'n':
            exit()