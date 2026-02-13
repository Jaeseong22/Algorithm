import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

citys = {i:[] for i in range(1, n+1)}
for _ in range(m):
    start, end, weight = map(int, input().split())
    citys[start].append((end, weight))

start_num, end_num = map(int, input().split())

distance = [INF] * (n+1)
distance[start_num] = 0
prev = [-1] * (n+1)

q = []
heapq.heappush(q, (0, start_num))

while q:
    dist, now = heapq.heappop(q)
    
    if dist > distance[now]:
        continue
    
    for nxt, cos in citys[now]:
        cost = dist + cos
        
        if cost < distance[nxt]:
            distance[nxt] = cost
            prev[nxt] = now
            heapq.heappush(q, (cost, nxt))

print(distance[end_num])
path = []
cur = end_num

while cur != -1:
    path.append(cur)
    cur = prev[cur]

path.reverse()
print(len(path))
print(*path)