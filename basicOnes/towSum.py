'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

**for example**:
Input: nums = [2,7,11,15], target = 9
Output: [0,1](because if we add num of position  0 & 1 we get 9)
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class solution(object):

    def twoSum(self,nums,target):
        dict={}
        for i in range(0,len(nums)):
            dict[nums[i]]=i

        for i in range(0,len(nums)):
            x=target-nums[i]
            if x in dict and i !=d[x]:
                return[i,dict[x]]

        return None
            
