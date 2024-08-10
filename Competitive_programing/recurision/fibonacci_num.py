<<<<<<< HEAD:competitive Programing-chatGpt/recurision/fibonacci_num.py
<<<<<<< HEAD
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/recurision/fibonacci_num.py
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
<<<<<<< HEAD:competitive Programing-chatGpt/recurision/fibonacci_num.py
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
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/recurision/fibonacci_num.py
print(fibonacci(36))