'''
Problem: Given an integer array numss, find the contiguous subarray (containing at least one numsber) which has the largest sum and return its sum.
'''

def maxsubarray(nums):
    if not nums :
        return nums
    max_sum=current_sum=nums[0]
    
    for num in nums[1:]:
        current_sum=max(num,current_sum+num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test the function
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsubarray(nums))  # Output: 6