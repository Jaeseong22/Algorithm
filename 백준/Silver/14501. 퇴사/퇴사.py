import sys
input = sys.stdin.readline

N = int(input())

graph = [(0, 0)]
for _ in range(N):
    t, p = map(int, input().split())
    graph.append((t, p))

dp = [0] * (N+2)

for i in range(1, N+1):
    dp[i + 1] = max(dp[i+1], dp[i])
    
    t, p = graph[i]
    end = i + t
    
    if end <= N+1:
        dp[end] = max(dp[end], dp[i] + p)

print(max(dp))