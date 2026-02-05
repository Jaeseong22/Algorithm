import sys
input = sys.stdin.readline
n = int(input())

tree = {i:[] for i in range(1, n+1)}

for _ in range(n-1):
    root, child, weight = map(int, input().split())
    tree[root].append((child, weight))
    tree[child].append((root, weight))

visited = [-1] * (n+1)

def dfs(start):
    stack = [(start, 0)]
    visited[start] = 0
    
    while stack:
        now, dist = stack.pop()
        
        for nxt, w in tree[now]:
            if visited[nxt] == -1:
                visited[nxt] = dist + w
                stack.append((nxt, visited[nxt]))
                
dfs(1)

last = visited.index(max(visited))
visited = [-1]*(n+1)
dfs(last)

print(max(visited))