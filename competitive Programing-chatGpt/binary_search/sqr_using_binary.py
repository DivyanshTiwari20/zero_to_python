'''
Write a function to find the square root of a number using binary search 
(integer part only)
'''

def integer_square_root(n):
    if n < 0:
        raise ValueError("Can't compute the square root of a negative number.")
    if n == 0 or n == 1:
        return n
    
    left, right = 0, n
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

print(integer_square_root(17))  # Output: 4
print(integer_square_root(16))  # Output: 4
print(integer_square_root(25))  # Output: 5
print(integer_square_root(1))   # Output: 1
print(integer_square_root(0))   # Output: 0
print(integer_square_root(2))   # Output: 1



