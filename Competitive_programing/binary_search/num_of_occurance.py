<<<<<<< HEAD:competitive Programing-chatGpt/binary_search/num_of_occurance.py
<<<<<<< HEAD
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/binary_search/num_of_occurance.py
'''
Write a function to find the number of occurrences of a target element in 
a sorted list using binary search. 
'''

def binary_search_first(arr, target):
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first_occurrence = mid
            right = mid - 1  # continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurrence

def binary_search_last(arr, target):
    left, right = 0, len(arr) - 1
    last_occurrence = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last_occurrence = mid
            left = mid + 1  # continue searching in the right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last_occurrence

def count_occurrences(arr, target):
    first = binary_search_first(arr, target)
    if first == -1:  # target not found in the array
        return 0
    last = binary_search_last(arr, target)
    return last - first + 1

# Example usage:
sorted_list = [1, 2, 2, 2, 3, 4, 5, 5, 6]
target = 2
print(count_occurrences(sorted_list, target))  # Output: 3
<<<<<<< HEAD:competitive Programing-chatGpt/binary_search/num_of_occurance.py
=======
'''
Write a function to find the number of occurrences of a target element in 
a sorted list using binary search. 
'''

def binary_search_first(arr, target):
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first_occurrence = mid
            right = mid - 1  # continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurrence

def binary_search_last(arr, target):
    left, right = 0, len(arr) - 1
    last_occurrence = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last_occurrence = mid
            left = mid + 1  # continue searching in the right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last_occurrence

def count_occurrences(arr, target):
    first = binary_search_first(arr, target)
    if first == -1:  # target not found in the array
        return 0
    last = binary_search_last(arr, target)
    return last - first + 1

# Example usage:
sorted_list = [1, 2, 2, 2, 3, 4, 5, 5, 6]
target = 2
print(count_occurrences(sorted_list, target))  # Output: 3
>>>>>>> c4f5223ba10d71953b90e01d93359193ccea7503
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/binary_search/num_of_occurance.py
