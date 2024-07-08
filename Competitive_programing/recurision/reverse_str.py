'''
    Write a recursive function to reverse a string.
'''

def reverse_str(s):
    if len(s)==0:
        return s
    else:
        # Here we used to bottom-up to reversed the string. Recurrsion return result from bottom to up. 
        return reverse_str(s[1:])+s[0]


print(reverse_str("hello"))  # Output: "olleh"
print(reverse_str("python")) # Output: "nohtyp"