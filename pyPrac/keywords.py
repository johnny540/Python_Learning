import keyword

kw = keyword.kwlist
print("Please choose category of keywords")
 
print("1. Flow Control")
print("2. Exception Handling")
print("3. Class")
print("4. Function and Method ")
print("5. Variable")
print("6. Object")
print("7. Module")
print("8. Check")
print("9. Built in Constants")
print("10.Logical")

choice = int(input("\nEnter Category Number: "))

fc = [20,14,13,17,32,8,10,30,34,28]
eh = [31,15,29,16,5]
cls = [9]
fm = [11,33,24]
var = [19,25]
obj = [12]
mdl = [21,18,4]
chk = [23,22]
bc = [2,0,1]
logical = [3,27,26]

if choice == 1 :
	for index in fc:
		if index == 17 or index == 8 or index == 34:
			print()
		print(kw[index])
elif choice == 2 :
	for index in eh:
		if index == 16:
			print()
		print(kw[index])
elif choice == 3 :
	print(kw[9])
elif choice == 4 :
	for index in fm :
		print(kw[index])

elif choice == 5 :
	for index in var :
		print(kw[index])

elif choice == 6 :
	for index in obj :
		print(kw[index])
elif choice == 7 :
	for index in mdl :
		print(kw[index])
elif choice == 8 :
	for index in chk :
		print(kw[index])
elif choice == 9 :
	for index in bc :
		print(kw[index])
elif choice == 10 :	
	for index in logical:
		print(kw[index])
"""
for i in range(len(kw)) : # To Print keywords along with index numbers
	print(i+1,kw[i])
"""	
