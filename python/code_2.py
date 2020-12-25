# program to arrange dictionary in accending order

data = {"aditya":85, "alan":89, "soman":75, "ravi":98, "lokesh":83}

a = []
for key, values in data.items():
    b = (key, values)
    a.append(b)
print(a)
print(sorted(a, key= lambda kv: (kv[1], kv[0])))