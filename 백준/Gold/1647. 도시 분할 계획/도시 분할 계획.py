import sys, heapq
INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())
roads = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    roads[A].append((B, C))
    roads[B].append((A, C))

visited = [False]*(N+1)
pq = [(0, 1)]
answer = 0
max_cost = 0

while pq:
    cost, now = heapq.heappop(pq)
    
    if visited[now]:
        continue
    visited[now] = True
    answer += cost
    max_cost = max(max_cost, cost)
    
    for nxt, weight in roads[now]:
        if not visited[nxt]:
            heapq.heappush(pq, (weight, nxt))

print(answer - max_cost)