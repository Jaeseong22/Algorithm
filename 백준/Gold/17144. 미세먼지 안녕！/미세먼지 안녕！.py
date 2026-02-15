import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cleaner = []
for i in range(R):
    if graph[i][0] == -1:
        cleaner.append(i)

top = cleaner[0]
bottom = cleaner[1]

for _ in range(T):

    temp = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:

                dust = graph[i][j] // 5
                cnt = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0<=nx<R and 0<=ny<C and graph[nx][ny] != -1:
                        temp[nx][ny] += dust
                        cnt += 1

                graph[i][j] -= dust * cnt

    for i in range(R):
        for j in range(C):
            if graph[i][j] != -1:
                graph[i][j] += temp[i][j]

    # 위쪽
    for i in range(top-1, 0, -1):
        graph[i][0] = graph[i-1][0]

    for i in range(C-1):
        graph[0][i] = graph[0][i+1]

    for i in range(top):
        graph[i][C-1] = graph[i+1][C-1]

    for i in range(C-1, 1, -1):
        graph[top][i] = graph[top][i-1]

    graph[top][1] = 0

    # 아래쪽
    for i in range(bottom+1, R-1):
        graph[i][0] = graph[i+1][0]

    for i in range(C-1):
        graph[R-1][i] = graph[R-1][i+1]

    for i in range(R-1, bottom, -1):
        graph[i][C-1] = graph[i-1][C-1]

    for i in range(C-1, 1, -1):
        graph[bottom][i] = graph[bottom][i-1]

    graph[bottom][1] = 0

    graph[top][0] = -1
    graph[bottom][0] = -1


answer = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)