
import sys
input = sys.stdin.readline

N = int(input())

polygon = [list(map(int, input().split())) for _ in range(N)]
sig = 0

for i in range(N):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i+1)%N]
    sig += x1*y2 - x2*y1
    
sig = abs(sig) /2
print(f"{sig:.1f}")