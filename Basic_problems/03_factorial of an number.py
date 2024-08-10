# Write a Python program to find the factorial of a given number. The user should input the number, and your program should calculate its factorial.

user_input = int(input("Enter a number to find its factorial:\n"))

# Initialize a variable to store the factorial, starting with 1
factorial_result = 1

# Calculate the factorial using a loop
for i in range(1, user_input + 1):
    factorial_result *= i

# Print the result
print(f"The factorial of {user_input} is: {factorial_result}")
