'''
Write a function to perform binary search on a sorted list and return the index of the target element (-1 if not found).

Binary search: Binary search is an efficient algorithm for finding the index of a target element in a sorted list. It works by repeatedly dividing the search interval in half.

'''

def binary_search(arr, target):
    low, high = 0, len(arr) - 1 # low vaue=0 and high = len of array
    while low <= high:
        mid = (low + high) // 2 # we are using "//" because we want int only. 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Test the function
print(binary_search([1, 3, 5, 7, 9], 5))  # Output: 2
print(binary_search([1, 3, 5, 7, 9], 6))  # Output: -1
print(binary_search([1, 3, 5, 7, 9], 9))  # Output: 4

        
    
