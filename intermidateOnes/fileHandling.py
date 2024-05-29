'''
Merging multiple text files into one requires knowledge of file handling in Python and handling exceptions.

'''

fileHandling=fileHandling_1="";

#Reading data from file one
with open("fileHandling","r") as fp:
	data=fp.read()

#Reading data from file two
with open("fileHandling_1","r")as fp:
	data2=fp.read()

'''Merging 2 files to add the data of 
files2 from the next line'''

data+="\n"
data+=data2

#we opened the 3rd file in "w" mode to create an new file 
with open("fileHandling_2","w")as fp:
	fp.write(data)