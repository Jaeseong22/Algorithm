import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().split())
distance = [-1]*(100001)
count = [0]*(100001)

q = deque()
q.append(N)
distance[N] = 0
count[N] = 1

while q:
    now = q.popleft()
    
    for n in (now+1, now-1, now*2):
        if n < 0 or n > 100000:
            continue
        if distance[n] == -1:
            distance[n] = distance[now] + 1
            count[n] = count[now]
            q.append(n)
        
        elif distance[n] == distance[now] + 1:
            count[n] += count[now]

print(distance[K])
print(count[K])