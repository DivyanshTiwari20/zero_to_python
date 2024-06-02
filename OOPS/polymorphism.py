'''Question: Create a base class Vehicle with a method num_wheels(). Create subclasses Car and Bike that override the num_wheels() method to return 4 and 2, respectively.'''

class Vechile:
    def num_wheels(self):
        pass
class Car(Vechile):
    def num_wheels(self):
        return 4
        
class Bike(Vechile):
    def num_wheels(self):
        return 2
        

print(Car().num_wheels())
print(Bike().num_wheels())