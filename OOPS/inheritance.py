'''Question: Create a class Animal with a method sound(). Create a subclass Dog that inherits from Animal and overrides the sound() method to print "Bark".'''


class Animal():
    def sound(self):
        print("some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

dog=Dog()
dog.sound()