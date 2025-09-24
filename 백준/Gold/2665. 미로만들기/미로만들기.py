from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

rooms = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

q = deque()
q.append((0, 0))
visited[0][0] = 1

def bfs():
    while q:
        r, c = q.popleft()
        if r == n - 1 and c == n - 1:
            print(visited[r][c] - 1)
            return
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if rooms[nr][nc] == 1:
                    visited[nr][nc] = visited[r][c]
                    q.appendleft((nr, nc))
                else:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

bfs()