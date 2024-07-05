'''
Write a function that takes a list of integers and returns a new list containing only the even numbers.
'''

def onlyEven(lst):
    return [num for num in lst if num %2==0]


print(onlyEven([4,6,7,8,9,1]))