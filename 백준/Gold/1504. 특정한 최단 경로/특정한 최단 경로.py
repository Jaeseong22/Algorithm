import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = {i : [] for i in range(1, N+1)}

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance

v1, v2 = map(int, input().split())

distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = distance[v1] + v1_distance[v2] + v2_distance[N]
v2_path = distance[v2] + v2_distance[v1] + v1_distance[N]

result = min(v1_path, v2_path)

print(result if result < INF else -1)