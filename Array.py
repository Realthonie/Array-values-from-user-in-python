from array import *

arr = array('i', [])

ask = int(input("Enter the length of the array:\n"))

for i in range(ask):
    x = int(input("Enter next value:\n"))
    arr.append(x)


print(arr)

# To look for the index number of a value in arr using for loop

val = int(input("Enter the value you want to search for its index:\n"))

k = 0
for e in arr:
    if e == val:
        print(k)
        break

    k += 1

# To look for the index number of a value in arr using a built-in function
print(arr.index(val))

# To delete a value by its index number
quest = int(input("Enter the index value you want to delete:\n"))

k = 0
for i in arr:
    if i == quest:
        del arr[i]

    k += 1

print(arr)

# To search for the index number of a value
search = int(input("Enter the value you wish to search for its index:\n"))

k = 0
for i in arr:
    if i == search:
        print(k)
        break
    k += 1