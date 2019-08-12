from array import *

n = int(input("Enter size of array "))
arr = array('i',[])

for i in range(n):
    print("Enter value:",i+1,": ",end="")
    val = int(input())
    arr.append(val)
print(arr)

srch = int(input("enter value to search: "))

k=0
for e in arr:
    if e==srch:
        print("index of ",srch, "is : ",k)
        break
    k += 1
else:
    print("Value not found")
