'''
Extracting words and corresponding numbers from a string requires good
string manipulation skills and regular expressions.

'''
#Python program to extract emails From 
# the String By Regular Expression.

#Importing module required for regular expressions.
import re

#Example string
sample='''
Jessica was determined to take her Python skills to the next level. She created a GitHub repository called "python-mastery" and began populating it with code examples, project ideas, and resources she found online. As she progressed, she started receiving contributions and feedback from other Python enthusiasts through the repository's issue tracker. Emails poured in from usernames like pythonrules@mail.com, codingwizard@example.net, and snakecharmers@python.org. Jessica diligently reviewed every suggestion, applying the ones that made sense and politely responding to queries from greencode@coder.com, pythonpadawan@learner.net, and py_jedi_123@gmail.com. Her repository slowly gained traction, attracting more contributors like data_guru@analytics.org and scicomp@math.edu. With each commit, Jessica's Python knowledge expanded, and she felt more confident tackling advanced topics like object-oriented programming, web development frameworks, and data analysis libraries.
'''

# \S matches any non-whitespace character  
# @ for as in the Email  
# + for Repeats a character one or more times  

findEmail=re.findall("\S+@\S+",sample)

#Printing the list
print(findEmail)