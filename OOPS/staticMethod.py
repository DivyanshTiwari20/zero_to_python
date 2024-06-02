'''Question: Create a class MathOperations with a static method add(a, b) that returns the sum of two numbers.'''

class MathOperations():
    @staticmethod
    def add(a,b):
        return a+b
    
print(MathOperations.add(5,6))