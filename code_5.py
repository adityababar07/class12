# write a program to edit the phone number of arvind in file phonebook.txt

import re , os

with open("phonebook.txt", "w") as f:

    no_of_entries = int(input("enter the no. of entries u have to do :\t")) 


    for _ in range(no_of_entries):
        entry1 = input("enter name of the person :\t")
        entry2 = int(input("enter the phone number of the person :\t"))
        entry = (f"{entry1} : {entry2}\n")
        f.write(entry)
f.close()
permmision = input("Do you want to edit phone numbers (y/n) :\t")

if permmision == "y":
    name = input("enter the name of the person who's phonenumber you want to edit :\t")
    with open("phonebook.txt", "r+") as f:
        for line in f:
            if name in line:
                a = line
                current_ph_no = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
                mo = current_ph_no.search(a)
                old_number = mo.group()
                print(f"Current number of {name} is {old_number}.")
                new_entry = int(input("enter the new phone number :\t"))
                new_no = f"{name} : {new_entry}\n"
                f.writelines(new_no)
    with open("phonebook.txt", "r") as f:
            data = f.readlines()
    with open("phonebook.txt", "w") as f:
        for line in data:
            if line.strip("\n") != f"{name} : {old_number}":
                f.write(line) 
else:
    print("thank you")
    exit()


