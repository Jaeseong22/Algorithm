import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
result = []

def dfs(v, num, visited = []):
    num += 1
    visited.append(v)
    
    if v == b:
        result.append(num)
    
    for i in graph[v]:
        if i not in visited:
            dfs(i, num, visited)
    
dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)