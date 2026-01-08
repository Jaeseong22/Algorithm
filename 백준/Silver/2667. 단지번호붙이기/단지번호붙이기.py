import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                cnt += dfs(nx, ny)
    return cnt

sizes = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            sizes.append(dfs(i, j))

print(len(sizes))
for s in sorted(sizes):
    print(s)