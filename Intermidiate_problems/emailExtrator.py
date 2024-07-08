'''Extracting email addresses using regular expressions requires 
understanding of regex patterns and string manipulation'''

#Importing re package of regular expression
import re

sample='''
In the virtual corridors of GitHub, Jessica’s “python-mastery” repository thrived. Emails arrived like coded whispers, each bearing a unique signature: pythonrules@mail.com, the enigmatic sage; codingwizard@example.net, weaving spells in loops; and snakecharmers@python.org, unraveling secrets from byte streams. Jessica’s Python journey unfolded, one commit at a time, as her knowledge blossomed like wildflowers in spring. 🌼🐍
'''

findEmail=re.findall("\S+@\S+",sample)

print(findEmail)


