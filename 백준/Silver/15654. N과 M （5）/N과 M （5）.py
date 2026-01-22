import sys
input = sys.stdin.readline

N, m = map(int, input().split())
n = list(map(int, input().split()))
n = sorted(n)
res = []

def dfs():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    
    for i in n:
        if i not in res:
            res.append(i)
            dfs()
            res.pop()
            
dfs()