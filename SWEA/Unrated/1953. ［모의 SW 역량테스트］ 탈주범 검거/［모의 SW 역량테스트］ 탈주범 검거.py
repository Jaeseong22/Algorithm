from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
oops = [1, 0, 3, 2]

pipes = {
    0: [],
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [1, 2],
    5: [0, 2],
    6: [0, 3],
    7: [1 ,3],
}

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    times = [[0]*(M) for _ in range(N)]
    times[R][C] = 1
    
    q = deque()
    q.append((R, C))
    ans = 1
    
    while q:
        x, y = q.popleft()
        if times[x][y] == L:
            continue
        for i in pipes[graph[x][y]]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and times[nx][ny] == 0:
                if oops[i] in pipes[graph[nx][ny]]:
                    times[nx][ny] = times[x][y] + 1
                    ans += 1
                    q.append((nx, ny))
    
    print(f"#{tc} {ans}")