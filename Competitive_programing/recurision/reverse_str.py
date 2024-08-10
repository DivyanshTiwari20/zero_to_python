<<<<<<< HEAD:competitive Programing-chatGpt/recurision/reverse_str.py
<<<<<<< HEAD
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/recurision/reverse_str.py
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
<<<<<<< HEAD:competitive Programing-chatGpt/recurision/reverse_str.py
=======
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
>>>>>>> c4f5223ba10d71953b90e01d93359193ccea7503
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/recurision/reverse_str.py
print(reverse_str("python")) # Output: "nohtyp"