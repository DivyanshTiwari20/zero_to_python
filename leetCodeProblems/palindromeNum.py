'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.
'''

class Solution:
    def isPalindrome(self,x:int)-> bool:
        converStrinInt=str(x)

        return converStrinInt==converStrinInt[::-1]

#Example usage:
solution=Solution()
print(solution.isPalindrome(828))
