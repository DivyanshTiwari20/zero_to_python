'''Guess the Number game using python!!'''


import random

secret_num=random.randint(1,100)

#Starting the game
print("Welcome to Guess_num game:\n");
print("I'm thinking of an number between 1 to 100.\n");

guess=None

# Variable to count the number of attempts
no_of_attempts=0;

# Loop until the user guesses the correct number
while guess!=secret_num:
    guess=int(input("Enter your number:\n"));
    
    # Increment the attempts counter
    no_of_attempts+=1;

    # Check if the guess is too low, too high, or correct
    if guess<secret_num:
        print("Too low! Try guessing a higher number.")
    elif guess>secret_num:
        print("Too high! Try guessing a lower number.")
    else:
        print(f"Congratulations! You guessed the correct number in {no_of_attempts} guess.")



print("Thanks for playing the game.")

# Happy Coding!!
