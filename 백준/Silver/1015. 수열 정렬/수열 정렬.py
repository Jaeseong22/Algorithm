import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

b = sorted(a)

res = []

for i in a:
    if i in b:
        res.append(b.index(i))
        b[b.index(i)] = -1
 
print(*res)