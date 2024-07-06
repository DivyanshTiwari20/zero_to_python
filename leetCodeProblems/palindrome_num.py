'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''

x=121
def isPalindrome(x):
    if x<0:
        return False
    i=x
    s=0
    while(i>0):
        d=i%10
        s=s*10+d
        i=i/10

    if x==s:
        return True
    return False

print(isPalindrome(121))