'''
Problem: A robot is located at the top-left corner of a `m x n` grid. The robot can only move either down or right at any point in time. How many possible unique paths are there to the bottom-right corner?
'''
def unique(m,n):
    dp=[[1]*n for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]

    return dp[-1][-1]

# Test the function
print(unique(3, 7))  # Output: 28