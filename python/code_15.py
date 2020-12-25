# write a program that reads character one by one and store them in UPPER if in upper case or in LOwer if in other.

def convertOpposite(str): 
    ln = len(str) 
    for i in range(ln): 
        if str[i] >= 'a' and str[i] <= 'z': 
  
            # Convert lowercase to uppercase 
            str[i] = chr(ord(str[i]) - 32) 
  
        elif str[i] >= 'A' and str[i] <= 'Z': 
  
            # Convert lowercase to uppercase 
            str[i] = chr(ord(str[i]) + 32) 
  
# Driver code 
if __name__ == "__main__": 
    str = input("Enter the sting :\t")
    str = list(str) 
  
    # Calling the Function 
    convertOpposite(str) 
  
    str = ''.join(str) 
    print(str) 
