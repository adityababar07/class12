# write a python code to demonstrate working of binary search in library

data = []
input0 = int(input("How much numbers you want to enter :\t"))
for _ in range(input0):
    input1 = int(input("Enter the no to the list :\t"))
    data.append(input1)
print(data)
print("List data is being sorted .....")
data.sort()
print(f"Sorted data is {data}.")

def findValue(data, number_to_find, low, high):
	if high >= low:
		middle = low + (high - low) // 2

		if data[middle] == number_to_find:
			return middle
		elif data[middle] < number_to_find:
			return findValue(data, number_to_find, middle + 1, high)
		else:
			return findValue(data, number_to_find, low, middle - 1)
	
	else:
		return -1

number_to_find = int(input("Enter the no. you want to search :\t"))
final = findValue(data, number_to_find, 0, len(data) - 1)

if final == -1:
	print("This item was not found in the list.")
else:
	print("The number " + str(number_to_find) + " was found at index position " + str(final) + ".")


# total_number_of_elements = len(data)
# median_index = (total_number_of_elements//2)
# part1 = data[0:median_index]
# part2 = data[median_index+1:]
# print(part1,part2)

# while True:
#     if data[median_index] == number:
#         print(f"Index number of {number} is {median_index}.")
#     elif :
        
