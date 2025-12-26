import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    res = []
    n = int(input())
    n = bin(n)
    n = n[2:]
    for i in range(len(n)):
        if n[i] == '1':
            res.append(len(n)-1-i)        
    res = sorted(res, reverse=False)
    
    print(*res)