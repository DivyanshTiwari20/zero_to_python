''' Task4 Fibonacci series for the (n) Number user will input'''

#If you want to find the fibonacci numbers under twenty.

# def fibonacci(n):
#     a,b=0,1
#     while a<=n:
#         print(a,end=' ') #using "end=' '" to make space between the numbers
#         a,b=b,a+b
        
# n=int(input("Enter you number:\n"))
# fibonacci(n)

#Another way if you want the first twenty numbers of fibonacci series in an loop.

def fibonacci(n):
    a,b=0,1
    for i in range (n):
        print(a,end=" ")
        a,b=b,a+b
    
while True:

    n=int(input("\nEnter a number:"))
    fibonacci(n)
    if n==0:
        break

