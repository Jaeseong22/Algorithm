import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
control = [
    (0,1), (0,-1), (1,0), (-1,0),
    (1,1), (-1,1), (1,-1), (-1,-1)
]
visited = [[False]*m for _ in range(n)]
cnt = 0

def dfs(x, y):
    visited[x][y] = True
    now = graph[x][y]
    flag = True
    stack = [(x, y)]
    
    while stack:
        x, y = stack.pop()
        for dx, dy in control:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] == now:
                    stack.append((nx, ny)) 
                    visited[nx][ny] = True
                elif graph[nx][ny] > now:
                    flag = False
    if flag:
        return True
    else:
        return False

for i in range(n):
    for j in range(m):
        if not visited[i][j] and dfs(i, j):
            cnt += 1
            
print(cnt)