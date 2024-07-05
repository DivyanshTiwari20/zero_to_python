'''
Question: Write a recursive function to compute the factorial of a number.
'''

def factorial(num):
    if (num==0 or num==1):
        return 1
    else:
        return num* factorial(num-1)#Calling fuction inside an fucntion.
    
print(factorial(5))

# Check the README file for detail explanaiton of the code.
