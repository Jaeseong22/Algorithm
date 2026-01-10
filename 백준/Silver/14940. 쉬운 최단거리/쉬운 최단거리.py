from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append((i, j))
            dist[i][j] = 0
        elif graph[i][j] == 0:
            dist[i][j] = 0
            
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if dist[nx][ny] == -1 and graph[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                
for i in range(n):
    print(*dist[i])