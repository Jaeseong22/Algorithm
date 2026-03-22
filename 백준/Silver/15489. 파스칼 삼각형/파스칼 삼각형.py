import sys
input = sys.stdin.readline

R, C, W = map(int, input().split())
dp = [[0]*(R+W+1) for _ in range(R+W+1)]
dp[1][1] = 1

for i in range(2, R+W+1):
    for j in range(1, i+1):
        if j == 1 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

result = 0
for i in range(R, R+W):
    for j in range(C, C + (i - R) + 1):
        result += dp[i][j]

print(result)