'''Taks3_Creating an Python script that generates a random number between 1 and 100. The user should have a limited number of attempts (e.g., 10 attempts) to guess the number. Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.'''

#importing random module
import random

#Giving min and max length of the numbers
min_value=1
max_value=100

#Using "random.randint" to get the whole number from 1 to 100 only from the random module
randomNum=random.randint(min_value,max_value)

#Setting the number of attempts to 5
attempts=5

#Print msg to user
print(f"Guess an Num between 1 to 100. You have 5 attempts only.") 

#loop through number of attempts
for i in range(attempts):
    guess=int(input("Enter your guess:\n"))

#checking if the guess is high or low
    if guess<randomNum:
        print("Low!")
    elif guess>randomNum:
        print("High!")
    else:
        print(f"Congratulations!You guess the number in {i+1}")
        break

else:
    print(f"Sorry!You lose the number is {randomNum}")