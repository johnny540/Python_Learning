from numpy import *

ar1 = array([1,2,3])
ar2 = array([3,4,5])
ar3 = array([])
for i in range(len(ar1)) :

	for j in range(len(ar2)) :

		if i==j :
			d = (ar1[i]+ar2[j])
			ar3[i] = d
print(type(ar1))
print(ar3)

