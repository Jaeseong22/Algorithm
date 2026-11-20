T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    n = int(input())
    x, y, d = 0, 0, 0
    graph = [[0]*n for _ in range(n)]
    graph[x][y] = 1
    
    for num in range(2, n*n+1):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if not (0<=nx<n and 0<=ny<n) or graph[nx][ny] != 0:
            d = (d+1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        
        x, y = nx, ny
        graph[x][y] = num
    
    print(f'#{tc}')
    for g in graph:
        print(*g) 