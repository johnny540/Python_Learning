from sys import *

# create a list by taking values at arguments
print()

lst =[]

for i in range(1,len(argv)) :
	lst.append(argv[i])

print(lst)
print()
# To print one by one
for i in lst:
	print(i)
