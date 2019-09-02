from sys import *

x = argv[1]
y = argv[2]

print(x+y) # By default argv[] returns string type if we try to add two arguments it will concatinate the two
print(int(x)+int(y))
print(type(x))
print(type(y))