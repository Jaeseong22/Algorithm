import sys
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    b = list(map(int, input().split()))
    b = sorted(b, reverse=True)
    res.append(b[2])

for x in res:
    print(x)