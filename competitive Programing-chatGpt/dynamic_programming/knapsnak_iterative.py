class solution:
    def knapSack(W,N, wt,val):
        dp=[[0]*(W+1) for i in range (N)]

        for i in range(N):
            for j in range(W+1):
                cap=j
                cwt=wt[i]
                cv=val[i]
                if i==0: # i==0 means we are in the first row
                    if cwt<=cap: #agar current weight <= captity to use (cv) ko dp me save karlo
                        dp[i][j]=cv
                    else:
                        dp[i][j]=0 # vana ap me 0 value save hogi means nothing.(same as previous, it is 0 initially)

                        # The above condition is to handel first row. 
                else:
                    if cwt<=cap:#Now for other row if current weight <= captity then we have 2 conditions
                        c1= cv+ dp[i-1][cap-cwt]
                        c2=dp[i-1][cap]
                        dp[i][j]=max(c1,c2)

                    else: #if if current weight !<=  capcity
                        dp[i][j]=dp[i-1][cap]
        return dp[N-1][W]
    
# Sample input
W = 10  # Weight capacity
N = 4   # Number of items
wt = [2, 3, 4, 5]  # Weights of items
val = [3, 4, 5, 6]  # Values of items

# Run the knapsack algorithm
result = solution.knapSack(W, N, wt, val)

print(f"Maximum value that can be obtained: {result}")