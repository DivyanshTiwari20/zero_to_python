'''Question: Create a class Temperature with a property celsius and a method to convert it to Fahrenheit.'''

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    def to_fahrenheit(self):
        return (self._celsius * 9/5) + 32

# Example usage
temp = Temperature(25)
print(temp.celsius)
print(temp.to_fahrenheit())
temp.celsius = 30
print(temp.to_fahrenheit())
