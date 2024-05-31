'''Question: Create a class Shape with a method area(). Create a subclass Square that overrides the area() method to calculate the area of the square.'''

class Shape():
    def area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

square=Square(5)
print(square.area())