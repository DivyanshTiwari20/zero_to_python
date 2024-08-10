<<<<<<< HEAD:competitive Programing-chatGpt/dynamic_programming/knapsnak.py
<<<<<<< HEAD
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/dynamic_programming/knapsnak.py
# def knapSack(self,W,wt,val,N):
#     dp={}
#     def sol(n,cap):
#         if n==0 or cap==0:
#             return 0
#         elif (n,cap) in dp:
#             return dp[(n,cap)]
#         else:
#             cwt=wt[n-1]
#             cv=val[n-1]
#             if cwt<=cap:
#                 c1=cv+sol(n-1,cap=cwt)
#                 c2=sol(n-1,cap)
#                 c= max(c1,c2)
#             else:
#                 c=sol(n-1,cap)

#                 dp[(n,cap)]=c
#                 return c
#         return sol(N,W)


class Solution:
    def knapSack(self, W, wt, val, N):
        dp = {}
        def sol(n, cap):
            if n == 0 or cap == 0:
                return 0
            elif (n, cap) in dp:
                return dp[(n, cap)]
            else:
                cwt = wt[n-1]
                cv = val[n-1]
                if cwt <= cap:
                    c1 = cv + sol(n-1, cap-cwt)
                    c2 = sol(n-1, cap)
                    c = max(c1, c2)
                else:
                    c = sol(n-1, cap)
                dp[(n, cap)] = c
                return c
        return sol(N, W)

# Create an instance of the Solution class
s = Solution()

# Sample input
W = 10
wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
N = 4

# Run the knapsack algorithm
result = s.knapSack(W, wt, val, N)

<<<<<<< HEAD:competitive Programing-chatGpt/dynamic_programming/knapsnak.py
=======
# def knapSack(self,W,wt,val,N):
#     dp={}
#     def sol(n,cap):
#         if n==0 or cap==0:
#             return 0
#         elif (n,cap) in dp:
#             return dp[(n,cap)]
#         else:
#             cwt=wt[n-1]
#             cv=val[n-1]
#             if cwt<=cap:
#                 c1=cv+sol(n-1,cap=cwt)
#                 c2=sol(n-1,cap)
#                 c= max(c1,c2)
#             else:
#                 c=sol(n-1,cap)

#                 dp[(n,cap)]=c
#                 return c
#         return sol(N,W)


class Solution:
    def knapSack(self, W, wt, val, N):
        dp = {}
        def sol(n, cap):
            if n == 0 or cap == 0:
                return 0
            elif (n, cap) in dp:
                return dp[(n, cap)]
            else:
                cwt = wt[n-1]
                cv = val[n-1]
                if cwt <= cap:
                    c1 = cv + sol(n-1, cap-cwt)
                    c2 = sol(n-1, cap)
                    c = max(c1, c2)
                else:
                    c = sol(n-1, cap)
                dp[(n, cap)] = c
                return c
        return sol(N, W)

# Create an instance of the Solution class
s = Solution()

# Sample input
W = 10
wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
N = 4

# Run the knapsack algorithm
result = s.knapSack(W, wt, val, N)

>>>>>>> c4f5223ba10d71953b90e01d93359193ccea7503
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/dynamic_programming/knapsnak.py
print(f"Maximum value that can be obtained: {result}")