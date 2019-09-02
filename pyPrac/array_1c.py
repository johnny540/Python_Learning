from numpy import *

"""
arr1 = array([1,2,3,4,5])
arr2 = array([5,6,7,8,9])

arr3 = arr1 +arr2 # it will add each elemetns in both arrays

print(arr3)
print("min",min(arr1))
print("max",max(arr1))
print("sin",sin(arr1))
print("cos",cos(arr1))
print("square",sqrt(arr1))
print("log",log(arr1))
print("sum",sum(arr1))
  
"""

#Copy Arrays
arr_a = array([5,1,8,7,9])
arr_b = arr_a  # copy but same address

print(arr_a)
print(arr_b)
#
print(id(arr_b))
print(id(arr_b))

# copy in with diffrent address

arr_c = arr_a.view() #its shallow copy if one array changed other array also changed

arr_a[1] = 9
print(arr_c)
print(id(arr_c))

#Deep Copy

arr_d = arr_a.copy()
arr_a[1] = 8
print(arr_d)


