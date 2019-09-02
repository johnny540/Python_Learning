
# Variable length arguments 

def person(name, *data) :

	print(name)

	for i in data :
		print(i)

person('johnny',28,'Ban')

# keyworded variable length argumnts

def person2(name,**data) :

	print(name)

	for i,j in data.items() :

		print(i,j)

person2('jani',age = 27,loc = 'Ban',mob = 949495656)