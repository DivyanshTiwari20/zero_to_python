'''
Problem: You are a robber planning to rob houses along a street. Each house has a certain amount of money stashed, and you cannot rob two adjacent houses. Find the maximum amount of money you can rob without alerting the police.

'''

def rob(num):
    if not num : # if num(list is empty) or house has no money we can't rob it  
        return 0
    n=len(num)
    if n==1: #if num of house are one we can only rob one house
        return num[0]
    #Above two are base conditions!!

    #dp depend on the list or num of houses
    dp=[0]*n #
    dp[0]=num[0]# if there are one house we can only one
    dp[1]=max(num[0],num[1]) # if there are two house take max of two 
    for i in range(2,n): 
        dp[i]= max(dp[i-1], dp[i-2] + num[i])# for greater houses first take max of two `dp[i-1],dp[i-2]`or also you have an choice that you wanna rob more or not `+num[i]`
    return dp[-1] #dp[-1] refers to the last element of the list which is maximam one


# Test the function
nums = [1, 2, 3, 1]
print(rob(nums))  # Output: 4