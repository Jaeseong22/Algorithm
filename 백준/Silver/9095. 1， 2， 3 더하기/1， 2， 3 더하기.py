import sys
input = sys.stdin.readline

def count(m):
    dp = [0] * (max(4, n+1))
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[m]

t = int(input())
for _ in range(t):
    n = int(input())
    print(count(n))