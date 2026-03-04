import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(u, parent):
    sub[u] = 1
    for v in tree[u]:
        if v == parent:
            continue
        dfs(v, u)
        sub[u] += sub[v]

N, R, Q = map(int, input().split())
tree = {i:[] for i in range(1, N+1)}
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    
sub = [0] * (N+1)
dfs(R, 0)
    
for _ in range(Q):
    U = int(input())
    print(sub[U])