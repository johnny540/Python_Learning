a = 10  # Global variable

def fun1() :

	""" if we want to change global variable inside function we need mension 
		"global" keyword bedore variable """
	 	
	global a
	a = 15   # Local Variable


	print("in function",a)













fun1()
print("Out side ",a)
