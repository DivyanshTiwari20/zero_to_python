#finding the max/min of the given range of numbers.

user_input=input("Enter your list of numbers seprated by spaces:\n")

numbers=[float(num)
         for num in user_input.split()]

max_value=max(numbers)
print("Maximum value:",max_value)

min_value=min(numbers)
print("Minimum value:",min_value)



