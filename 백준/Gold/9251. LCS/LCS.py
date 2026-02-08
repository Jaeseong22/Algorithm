import sys
input = sys.stdin.readline

fir = input().strip()
sec = input().strip()

dp = [[0] * (len(sec)+1) for _ in range(len(fir)+1)]

for i in range(1, len(fir)+1):
    for j in range(1, len(sec)+1):
        if fir[i-1] == sec[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(fir)][len(sec)])