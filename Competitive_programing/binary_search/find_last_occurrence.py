'''
Write a function to find the last occurrence of a target element in a 
sorted list using binary search.


    Find the last occurrence of target element in sorted list using Binary Search

    Args:
        arr(list): The sorted list to search
        target(int): The target element to find


    Returns: 
        (int): The index of the last occurrence of targer element,or -1 in case of not found.

'''

def last_occurrence(arr,target):
    lower,higher=0,len(arr)-1

    while lower<=higher:
        mid= (lower+higher)//2

        if arr[mid]==target:
            # If the current element is the target, check if it's the last occurrence
            if mid==0 or arr[mid+1]!=target:
                return mid
            else:
                 # If the current element is not the last occurrence, search the left half
                lower=mid+1
        elif arr[mid]<target:
            # If the current element is less than the target, search the right half
            lower=mid+1

        else:
            # If the current element is greater than the target, search the left half
            higher=mid-1

        # If the target element is not found, return -1
    return -1

my_list = [1, 2, 3, 3, 3, 4, 5]
print(last_occurrence(my_list, 3))  # Output: 4
print(last_occurrence(my_list, 6))  # Output: -1