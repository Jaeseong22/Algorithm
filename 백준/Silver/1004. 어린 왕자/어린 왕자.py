import sys
input = sys.stdin.readline
import math

t = int(input())
res = [0] * t
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for j in range(n):
        cnt = 0
        cx, cy, r = map(int, input().split())
        dx1 = x1 - cx 
        dy1 = y1 - cy
        dx2 = x2 - cx
        dy2 = y2 - cy
        d1 = dx1*dx1 + dy1*dy1
        d2 = dx2*dx2 + dy2*dy2
        
        if math.sqrt(d1) < r and math.sqrt(d2) > r:
            cnt += 1
        elif math.sqrt(d1) > r and math.sqrt(d2) < r:
            cnt += 1
        res[i] += cnt

for i in res:
    print(i)        