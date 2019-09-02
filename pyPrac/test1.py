s = "Johnny Kagitha"
r = []
s1 = s.split()

for o in s1 :
	print(o)

	for i in range(-1,-len(o)-1,-1) :
		r.append(o[i])


	
#print(r)
str = "".join(r)
print(str)
