from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            q.append((y, x))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while q:
    y, x = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n:
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))

ans = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            print(-1)
            exit()
        ans = max(ans, graph[y][x])

print(ans-1)