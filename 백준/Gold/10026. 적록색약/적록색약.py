import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

stack = []
def dfs(x, y):
    visited[x][y] = True
    stack.append((x, y))
    nowColor = graph[x][y]
    
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == nowColor and not visited[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True

normal_cnt = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            dfs(x, y)
            normal_cnt += 1


visited = [[False]*n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if graph[x][y] == 'G':
            graph[x][y] = 'R'


cnt = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            dfs(x, y)
            cnt += 1

print(normal_cnt, cnt)