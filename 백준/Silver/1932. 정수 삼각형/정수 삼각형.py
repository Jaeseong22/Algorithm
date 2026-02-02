import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    lis = list(map(int, input().split()))
    graph.append(lis)

dp = [[0]*i for i in range(1, n+1)]

dp[0][0] = graph[0][0]
if n == 1:
    print(dp[0][0])
    sys.exit()

dp[1][0] = dp[0][0] + graph[1][0]
dp[1][1] = dp[0][0] + graph[1][1]

if n == 2:
    print(max(dp[1][0], dp[1][1]))
    sys.exit()

for i in range(2, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = graph[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = graph[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = max(graph[i][j] + dp[i-1][j], graph[i][j] + dp[i-1][j-1])
            
print(max(dp[n-1]))