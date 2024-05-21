'''Task7_Write a function that takes a list as its argument and returns a new list that contains all the unique elements of the input list.'''


def remove_common_elements(list1, list2):
    # Create an empty list to store the non-common elements
    non_common_list = []
    
    # Loop through each element in the first list
    for value in list1:
        # Check if the element is not in the second list
        if value not in list2:
            # If it's not, add it to the non-common list
            non_common_list.append(value)
    
    # Return the non-common list
    return non_common_list

list1 = ["one", "two", "six"]
list2 = ["one", "eight", "ten", "six"]

list3 = remove_common_elements(list1, list2)
list4 = remove_common_elements(list2, list1)

list5 = list3 + list4

print(list5)