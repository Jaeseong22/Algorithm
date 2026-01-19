import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0

def dfs(x, y, depth, total):
    global ans
    if depth == 4:
        ans = max(ans, total)
        return
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, depth+1, total+graph[nx][ny])
                visited[nx][ny] = False

def check_t(x, y):
    global ans
    center = graph[x][y]
    wings = []
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            wings.append(graph[nx][ny])
    if len(wings) >= 3:
        wings.sort(reverse=True)
        ans = max(ans, center+wings[0]+wings[1]+wings[2])
        
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False
        check_t(i, j)
        
print(ans)