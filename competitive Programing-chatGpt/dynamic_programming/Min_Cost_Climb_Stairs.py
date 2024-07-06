'''
Problem: Given an array `cost` where `cost[i]` is the cost of `i-th` step, you need to find the minimum cost to reach the top of the floor. You can either start from the step with index 0 or index 1.
'''

def minCostClimbingStairs(n):
    n=len(cost)
    dp=[0]*(n+1)

    for i in range(2,n+1):
        dp[i]= min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    return dp[n]


# Test the function
cost = [10, 15, 20]
print(minCostClimbingStairs(cost))  # Output: 15
