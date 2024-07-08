# #----------------------Count the number of vowels in the sentence--------------------
# def count_vowels(sentence):
#     vowel_count=0

#     vowel=set("aeiouAEIOU")

#     for char in sentence:
#         if char in vowel:
#             # vowel_count=vowel_count+1
#             vowel_count+=1 
    
#     return vowel_count

# # geting user input
# sentence=input("Enter your sentence:\n")

# # calling the function
# result=count_vowels(sentence)

# -----------Reversing the order-------------------
def reverse(sentence):
    # spliting the sentence into list of words
    words = sentence.split()

    # reverse the order
    reversed_sentence = " ".join(words[::-1])

    return reversed_sentence

# calling the function
sentence = input("Enter your sentence:\n")
reversed_sentence = reverse(sentence)

# printing the result
print("Reversed order of words:", reversed_sentence)




