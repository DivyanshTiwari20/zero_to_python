'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

***********
You have two different ways to solve this problem 
1. Brute forec - Going to take an lot of time and storage (not effeicient)
2. hash_map- Effeicient way.

'''

nums = [2,7,11,15]
target=18

def two_sum(nums,target):
    hash_map={}

    for i,num in enumerate(nums):# enumerate fun is used to print index of numbers
        if target-num in hash_map:
            return [hash_map[target-num],i]
        hash_map[num]=i
        
    return []

print(two_sum(nums,target))