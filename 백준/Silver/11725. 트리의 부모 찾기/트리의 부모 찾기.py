from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = {i:[] for i in range(n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
parent = [0] * (n+1)
visited = [False] * (n+1)

q = deque()
q.append(1)
visited[1] = True

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            q.append(nxt)
        
for i in range(2, n+1):
    print(parent[i])