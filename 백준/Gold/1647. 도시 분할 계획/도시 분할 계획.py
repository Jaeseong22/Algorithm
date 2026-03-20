import sys
input = sys.stdin.readline

N, M = map(int, input().split())

roads = []

for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((C, A, B))

roads.sort()

parent = [i for i in range(N+1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a
    
result = 0
c = 0

for cost, a, b in roads:
    if find(a) != find(b):
        union(a, b)
        result += cost
        c = max(c, cost)

print(result - c)