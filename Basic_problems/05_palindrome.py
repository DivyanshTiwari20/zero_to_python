#checking whether the string is palindrome or !.
user_input=input("Enter your word/Sentence:\n")

clean_string="".join(user_input.split()).lower()

if clean_string==clean_string[::-1]:
    print("yes")
else:
    print("no")