from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False]*(n+1)
    visited[start] = True
    que = deque([start])
    cnt = 1
    
    while que:
        x = que.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                cnt += 1
    return cnt

max_cnt = 0
result = []

for i in range(1, n+1):
    c = bfs(i)
    if c > max_cnt:
        max_cnt = c
        result = [i]
    elif c == max_cnt:
        result.append(i)
        
print(*result)