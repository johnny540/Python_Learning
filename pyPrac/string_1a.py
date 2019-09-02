s = "Hi Johnny How are you"

print(s)
print(s[3])  # we can access string characters by using indexing

# In indexing If we try to access out of range then it will give out of index error

print(s[3:9]) # we can access string characters by using slicing

# In slicing If we try to access out of range it will not give error
 
print(s[-1:-8:-2]) 

# to print name one by one we can use loop

for i in s :
	print(i)
