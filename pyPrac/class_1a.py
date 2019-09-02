'''
emp_names = ['Johnny','anil','vasanth']
emp_sal = [35000,25000,18000]
emp_loc = ['Ban','Hyd','Vja']'''

class Emp :

	def __init__(self,name,sal,loc) :

		self.name = name
		self.sal = sal
		self.loc = loc

	def emp_details(self):
		print('*'*25)
		print("Employ name is ",self.name)
		print("Employ sal is ",self.sal)
		print("Employ loc is ",self.loc)
		print('*'*25)



e1 = Emp('Johnny',55000,'Ban')
e1.emp_details()



















