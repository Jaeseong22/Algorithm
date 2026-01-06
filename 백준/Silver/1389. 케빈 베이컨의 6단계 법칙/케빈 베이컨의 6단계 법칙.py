from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start):
    distance = [-1] * (n+1)
    distance[start] = 0
    q = deque([start])
    while q:
        x = q.popleft()
        for i in graph[x]:
            if distance[i] == -1:
                distance[i] = distance[x] + 1
                q.append(i)
    return sum(distance[1:])

min_val = float('inf')
result = 0
for i in range(1, n+1):
    a = bfs(i)
    if min_val > a:
        min_val = a
        result = i

print(result)