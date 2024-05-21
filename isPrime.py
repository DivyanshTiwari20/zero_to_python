'''Task9_Write a Python program that takes a number as input and checks if it is prime or not using a while loop.'''
#Taking an input from the user
userInput=int(input("Enter your number:\n"))

#Starting an Loop
for i in range(2,userInput):
    if userInput%i ==0:
        print("not Prime")
        #If the number is divisible by any num in (i) break the loop
        break

#We aren't using else in if statement because otherwise it will start printing only Prime in loop.
else:
    print("Prime")


'''ALSO THERE IS MORE EFFICIENT WAY OF DOING THE SAME THING BY DIVIDING THE NUM BY HALF(N/2). BUT I USED THIS BECAUSE AT THIS MOVEMENT I AN ONLY THINK OF THIS'''
