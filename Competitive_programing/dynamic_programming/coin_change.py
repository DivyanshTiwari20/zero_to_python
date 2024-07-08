'''
Problem: You are given coins of different denominations and a total amount of money. Write a function to compute the fewest number of coins that you need to make up that amount.
'''

def coinchange(coin,amount):
    dp=[float("inf")]*(amount+1)
    dp[0]=0
    for coin in coins:
        for x in range(coin,amount+1):
            dp[x]=min(dp[x],dp[x-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1


# Test the function
coins = [1, 2, 5]
amount = 11
print(coinchange(coins, amount))  # Output: 3