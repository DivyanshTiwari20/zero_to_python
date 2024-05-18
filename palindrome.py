'''To check whether the give phase or sentence is palindrome or not by taking input from the user.'''


#Creating an function to check to whether word is palindrome or not 
def palindrome(s):
    return s==s[::-1]#This line will check if reverse of userInput is eqall to it or not


#Taking input from user
s=input("Enter your phase/word\n")

#Saving the fucntion in an variable
funVar=palindrome(s)

#Using if/else to check the possibility
if funVar:
    print("yes")
else:
    print("no")

