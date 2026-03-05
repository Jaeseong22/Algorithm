import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

left = 0
right = N-1

best = float('inf')
answer = (0, 0)

while left < right:
    s = liquid[left] + liquid[right]
    
    if abs(s) < best:
        best = abs(s)
        answer = (liquid[left], liquid[right])
    
    if s < 0:
        left += 1
    else:
        right -= 1

print(*answer)