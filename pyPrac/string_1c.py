"""
Finding substrings:
 We can find a sub string in two directions like forward and backward direction.
 We can use the following 4 methods
For forward direction:
 find()
 index()
For backward direction:
 rfind()
 rindex()

"""

s = "Python programming language"
print(s)
	
print(s.find('p'))
print(s.find('P'))
print(s.find('Hello'))
print(s.find('o',1,15))  # nameofthestring.find(substring, begin, end)
