import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]

visited = [[False]*n for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, color):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

white = 0
black = 0

for i in range(m):        
    for j in range(n):    
        if not visited[i][j]:
            size = bfs(i, j, graph[i][j])
            if graph[i][j] == 'W':
                white += size * size
            else:
                black += size * size

print(white, black)