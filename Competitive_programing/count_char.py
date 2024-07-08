'''
Question: Write a function that takes a string and returns a dictionary with the count of each character in the string.
'''

def countchar(s):
    dict={}#initially dict in empty
    for char in s:
        if char in dict:#if char is in dict, increase count of that num otherwise.. save that char to dict
            dict[char]+=1
        else: 
            dict[char]=1
    return dict

#calling the function
print(countchar("harsh"))
        