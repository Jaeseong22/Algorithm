import sys
input = sys.stdin.readline

sub = 1000000007
n = int(input())

dp = [0, 1, 1, 2]

if n == 0 or n == 1 or n == 2:
    print(dp[n])
else: 
    for i in range(4, n+1):
        dp.append((dp[i-1]+dp[i-2])%sub)

print(dp[n])