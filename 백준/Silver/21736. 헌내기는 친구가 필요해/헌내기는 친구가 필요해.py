import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0 ,-1]
ch = [[0]* m for _ in range(n)]

campus = []
q = deque()

for i in range(n):
    campus.append(list(map(str, input().strip())))

    for j in range(len(campus[i])):
        if campus[i][j] == 'I':
            q.append((i, j))
            ch[i][j] = 1

answer = 0

while q:
    for _ in range(len(q)):
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and ch[nr][nc] == 0 and campus[nr][nc] != 'X':
                if campus[nr][nc] == 'P':
                    answer += 1
                ch[nr][nc] = 1
                q.append((nr, nc))
if answer == 0:
    print('TT')
else:
    print(answer)