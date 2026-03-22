import sys
input = sys.stdin.readline
r, g, b = 0, 1, 2
INF = int(1e9)

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
answer = INF

for color in (r, g, b):
    dp = [[0] * (3) for _ in range(N+1)]

    dp[1] = [INF] * 3
    dp[1][color] = house[0][color]
    
    for i in range(2, N+1):
        dp[i][r] = min(dp[i-1][g], dp[i-1][b]) + house[i-1][r]
        dp[i][g] = min(dp[i-1][r], dp[i-1][b]) + house[i-1][g]
        dp[i][b] = min(dp[i-1][r], dp[i-1][g]) + house[i-1][b]
    dp[N][color] = INF
    answer = min(answer, min(dp[N]))

print(answer)