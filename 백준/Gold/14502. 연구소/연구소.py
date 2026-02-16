from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 세로 M: 가로

graph = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for k in range(M):
            if graph[i][k] == 0:
                graph[i][k] = 1
                make_wall(count+1)
                graph[i][k] = 0

def bfs():
    q = deque()
    changed = []

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                q.append((i,j))

    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if 0<=nr<N and 0<=nc<M and graph[nr][nc]==0:
                graph[nr][nc] = 2
                changed.append((nr,nc))
                q.append((nr,nc))

    count = sum(row.count(0) for row in graph)

    global result
    result = max(result, count)

    for r,c in changed:
        graph[r][c] = 0
    
result = 0
make_wall(0)
print(result)