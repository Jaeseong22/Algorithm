T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, ch):
    global MAX
    MAX = max(MAX, visited[x][y])

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0<=nx<N and 0<=ny<N) or visited[nx][ny]:
            continue

        if graph[nx][ny] < graph[x][y]:              # 그냥 내려갈 수 있으면
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, ch)
            visited[nx][ny] = 0

        elif not ch and graph[nx][ny] - K < graph[x][y]:   # 깎으면 내려갈 수 있으면
            original = graph[nx][ny]
            graph[nx][ny] = graph[x][y] - 1          # 딱 한 칸 낮게만 깎기
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, True)
            visited[nx][ny] = 0
            graph[nx][ny] = original                 # 되돌리기

for tc in range(1, T+1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_g = 0

    max_c = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] > max_g:
                max_g = graph[i][j]
                max_c = [(i, j)]
            elif graph[i][j] == max_g:
                max_c.append((i, j))

    MAX = 0
    visited = [[0] * N for _ in range(N)]
    for x, y in max_c:
        visited[x][y] = 1
        dfs(x, y, False)
        visited[x][y] = 0

    print(f'#{tc} {MAX}')