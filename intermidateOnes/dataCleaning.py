'''
Write a function that takes a list of dictionaries representing data records and a 
dictionary of data types, and converts all values to the specified data types. 
Handle type conversion errors gracefully.

Example: convert_data([{"age": "25", "height": "5.8"}], {"age": int, "height": float}).
'''

dict={
	"name":"Divyansh",
	"age":25,
	"height":5.6,
}

nameType=type(dict["name"])
ageType=type(dict["age"])
heightType=type(dict["height"])



print(nameType)
print(ageType)
print(heightType)