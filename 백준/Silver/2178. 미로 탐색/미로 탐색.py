from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    dist = [[0]*m for _ in range(n)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 1
    while q:
        a, b = q.popleft()
        
        if a == n-1 and b == m-1:
            return dist[a][b]
        
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0<=na<n and 0<=nb<m:
                if dist[na][nb] == 0 and graph[na][nb] == 1:
                    dist[na][nb] = dist[a][b] + 1
                    q.append((na, nb))

print(bfs(0,0))