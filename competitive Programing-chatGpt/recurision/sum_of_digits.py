<<<<<<< HEAD
'''
Write a recursive function to sum the digits of a number.
'''

def sum_of_digit(n):
    if n==0:
        return 0
    elif n<0:
        return "Invalid Input"
    else:
        return n%10 + sum_of_digit(n//10)
    
=======
'''
Write a recursive function to sum the digits of a number.
'''

def sum_of_digit(n):
    if n==0:
        return 0
    elif n<0:
        return "Invalid Input"
    else:
        return n%10 + sum_of_digit(n//10)
    
>>>>>>> c4f5223ba10d71953b90e01d93359193ccea7503
print(sum_of_digit(123))