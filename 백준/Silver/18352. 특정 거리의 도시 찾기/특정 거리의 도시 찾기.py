from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
def bfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    q = deque([start])
    result = []
    while q:
        t = q.popleft()
        if visited[t] == k:
            result.append(t)
            continue
        for nxt in graph[t]:
            if visited[nxt] == -1:
                visited[nxt] = visited[t] + 1
                q.append(nxt)
    return result  
ans = bfs(x)  

if ans:
    for city in sorted(ans):
        print(city)
else:
    print(-1)