import sys
input = sys.stdin.readline

V = int(input())

tree = [[] for _ in range(V+1)]
for _ in range(V):
    lis = list(map(int, input().split()))
    for i in range(1, len(lis)-1, 2):
        adj = lis[i]
        weight = lis[i+1]
        tree[lis[0]].append((adj, weight))

def dfs(start):
    visited = [-1] * (V+1)
    visited[start] = 0
    stack = [(start, 0)]
    
    while stack:
        now, dist = stack.pop()
        
        for i in tree[now]:
            if visited[i[0]] == -1:
                nxt, cost = i[0], i[1]+dist
                visited[nxt] = cost
                stack.append((nxt, cost))
    
    return visited.index(max(visited)), max(visited)

node, dist = dfs(1)

d, diameter = dfs(node)

print(diameter)