<<<<<<< HEAD
'''
Write a recursive function to compute the nth Fibonacci number.
'''

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
=======
'''
Write a recursive function to compute the nth Fibonacci number.
'''

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
>>>>>>> c4f5223ba10d71953b90e01d93359193ccea7503
print(fibonacci(36))