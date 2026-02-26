from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
distance = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    distance[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0))
    
    while q:
        x, y, wall = q.popleft()
        
        if x == N-1 and y == M-1:
            return distance[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 0 and distance[nx][ny][wall] == 0:
                    distance[nx][ny][wall] = distance[x][y][wall] + 1
                    q.append((nx, ny, wall))
                
                if graph[nx][ny] == 1 and wall == 0:
                    distance[nx][ny][1] = distance[x][y][wall] + 1
                    q.append((nx, ny, 1))
    
    return -1

print(bfs())