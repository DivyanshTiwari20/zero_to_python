'''Task8_Write a function that takes a string as its argument and returns a dictionary that contains the count of each vowel in the input string. The dictionary keys should be the vowels and the values should be the counts'''


def vowelCount(userInput):
    #Intialize dictionary with vowels as keys
    vowelDict={"a":0, "e":0,"i":0,"o":0,"u":0}
    #Loop through each character in input string 
    for char in userInput:
        # If the character is a vowel, increment its count in the dictionary
        if char.lower() in vowelDict:
            vowelDict[char.lower()]+=1

    return vowelDict

#Taking input from the user
userInput=input("Enter your desire phase:\n")

vowelCount=vowelCount(userInput)

#Running the Function
print(vowelCount)
