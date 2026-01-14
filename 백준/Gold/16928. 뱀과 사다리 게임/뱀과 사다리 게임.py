from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
move = dict()

for _ in range(n):
    a, b = map(int, input().split())
    move[a] = b

for _ in range(m):
    u, v = map(int, input().split())
    move[u] = v

visited = [-1]*101
visited[1] = 0
q = deque([1])

while q:
    cur = q.popleft()
    if cur == 100:
        break
    for dice in range(1, 7):
        nxt = cur + dice
        if nxt > 100:
            continue
        if nxt in move:
            nxt = move[nxt]
            
        if visited[nxt] == -1:
            visited[nxt] = visited[cur] + 1
            q.append(nxt)
print(visited[100])