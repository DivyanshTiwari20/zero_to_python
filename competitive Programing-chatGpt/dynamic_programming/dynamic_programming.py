'''
Write a function to compute the nth Fibonacci number using dynamic programming.

Dynamic Programming: A method for solving complex problems by breaking them down into simpler sub-problems in a recursive manner.
'''

import time
import sys

# Recursive method with memoization
def fib(n, dp):
    if n == 0 or n == 1:
        return n
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
        return dp[n]

# Measure execution time and memory usage for recursive method
start_time = time.time()
dp = [-1] * 10
fib_result = fib(9, dp)
end_time = time.time()
print(fib_result)
print("Recursive method time:", end_time - start_time)
print("Recursive method memory usage:", sys.getsizeof(dp), "bytes")

# Iterative method
start_time = time.time()
dp = [0] * 101
dp[0] = 0
dp[1] = 1
for i in range(2, 101):
    dp[i] = dp[i - 1] + dp[i - 2]
iterative_result = dp[9]
end_time = time.time()
print(iterative_result)
print("Iterative method time:", end_time - start_time)
print("Iterative method memory usage:", sys.getsizeof(dp), "bytes")



