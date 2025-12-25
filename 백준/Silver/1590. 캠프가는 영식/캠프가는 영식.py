import sys
input = sys.stdin.readline

n, t = map(int, input().split())
ans = float('inf')

for _ in range(n):
    s, i, c = map(int, input().split())
    
    last = s + i * (c-1)
    if t > last:
        continue
    
    if t <= s:
        wait = s - t
    else:
        k = (t - s + i - 1) // i
        bus_time = s + i * k
        wait = bus_time - t
        
    ans = min(ans, wait)

print(ans if ans != float('inf') else -1)