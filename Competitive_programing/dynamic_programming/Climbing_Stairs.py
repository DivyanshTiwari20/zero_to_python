'''
    Problem: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

def climb_stair(n,dp):
    if n<=2:
        return dp[n]
    
    elif dp[n]!=0:
        return dp[n]
    else:
        dp[n] =climb_stair(n-1,dp)+climb_stair(n-2,dp)
        return dp[n]

n=100  
dp=[0]*(n-1)
dp[1] = 1
dp[2] = 2
print(climb_stair(5,dp)) #OUTPUT 8
