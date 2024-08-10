#Task2_Making an Simple Calc

#Getting inputs from the user for the numbers and the operation.
firstNum=int(input ("Enter the first number:\n"))
secNum=int(input ("Enter the second number:\n"))
userInput=int(input ("**select operaiton**\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))

#Using if/elif statements to perform the logic
if userInput==1:
    print(f"The Addition of {firstNum} and {secNum} is {firstNum+secNum}")#Using f string for the variables that user will give
elif userInput ==2:
    print(f"The Substraction of {firstNum} and {secNum} is {firstNum-secNum}")
elif userInput==3:
    print(f"The Multiplication of {firstNum} and {secNum} is {firstNum*secNum}")
elif userInput==4:
   print(f"The Division of {firstNum} and {secNum} is {firstNum/secNum}")


#Thank you...

