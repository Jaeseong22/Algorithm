import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
computers = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    computers[a].append((b, c))
    computers[b].append((a, c))

q = []
q.append((0, 1))
visited = [False] * (N+1)
result = 0

while q:
    cost, now = heapq.heappop(q)
    
    if visited[now]:
        continue
    visited[now] = True
    result += cost
    
    for nxt, w in computers[now]:
        heapq.heappush(q, (w, nxt))
        
print(result)