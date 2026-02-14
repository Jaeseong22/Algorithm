import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

N, M, X = map(int, input().split())
roads = [[] for _ in range(N+1)]
rev_roads = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, T = map(int, input().split())
    roads[a].append((b, T))
    rev_roads[b].append((a, T))

def dijkstra(X, graph):
    distance = [INF] * (N+1)
    distance[X] = 0
    q = []
    heapq.heappush(q, (0, X))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        
        for nxt, weight in graph[now]:
            cost = dist + weight
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    
    return distance

go = dijkstra(X, roads)

back = dijkstra(X, rev_roads)

answer = 0

for i in range(1, N+1):
    answer = max(answer, go[i] + back[i])

print(answer)