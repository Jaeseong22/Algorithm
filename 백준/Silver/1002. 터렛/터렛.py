import sys
import math
input = sys.stdin.readline

t = int(input())
res = []
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)) 
    if d == 0 and r1 == r2:
        res.append(-1)
    elif d==0 and r1 != r2:
        res.append(0)
    elif d < abs(r1 - r2) or d > (r1 + r2):
        res.append(0)
    elif d == abs(r1 - r2) or d == (r1 + r2):
        res.append(1)
    else:
        res.append(2)
    
for i in res:
    print(i)