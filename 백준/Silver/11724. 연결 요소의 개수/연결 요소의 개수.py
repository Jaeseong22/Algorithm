import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1      # 새 연결 요소 발견!
        dfs(i)

print(count)