'''Question: Define a class called Person with attributes name and age. 
Create an object of the class and print the name and age.'''

class Person():
	def __init__(self,name,age):
		self.name=name,
		self.age=age


person=Person("harsh",20)
print(person.name)
print(person.age)