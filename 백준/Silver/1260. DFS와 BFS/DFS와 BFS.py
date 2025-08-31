import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, n + 1):
    adj[i].sort()

# DFS (재귀)
sys.setrecursionlimit(10**6)
dfs_order = []
visited = [False] * (n + 1)

def dfs(x: int):
    visited[x] = True
    dfs_order.append(x)
    for nx in adj[x]:
        if not visited[nx]:
            dfs(nx)

dfs(v)

# BFS (큐)
bfs_order = []
visited = [False] * (n + 1)
q = deque([v])
visited[v] = True

while q:
    cur = q.popleft()
    bfs_order.append(cur)
    for nx in adj[cur]:
        if not visited[nx]:
            visited[nx] = True
            q.append(nx)

print(*dfs_order)
print(*bfs_order)