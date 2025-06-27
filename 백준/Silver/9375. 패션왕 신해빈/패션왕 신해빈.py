from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = defaultdict(int)

    for _ in range(n):  
        a, b = input().split()
        dp[b] += 1

    result = 1

    for x in dp:
        result *= (dp[x] + 1)

    print(result - 1)