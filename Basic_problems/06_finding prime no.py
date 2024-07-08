#finding an prime no upto an given number

user_input = int(input("Enter your number:\n"))

# Check if the number is greater than 1
if user_input > 1:
    # Start a loop from 2 up to the square root of the number
    for i in range(2, int(user_input**0.5) + 1):
        # Check if the number is divisible by 'i' without any remainder
        if user_input % i == 0:
            print('No, it is not a prime number')  # If divisible, it's not a prime number
            break  # Exit the loop because we already found a divisor
    else:
        # This block is executed if the loop completes without finding a divisor
        print('Yes, it is a prime number')
else:
    # If the number is 1 or less, it's not a prime number
    print('No, it is not a prime number')
