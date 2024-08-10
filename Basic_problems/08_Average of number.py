# finding the average of the given numbers 

user_input=(input("Enter your list of numbers:\n"))
numers=[float(num)
        for num in user_input.split()]

a=sum(numers)/len(numers)
print(a)