import sys
input = sys.stdin.readline

N, S = map(int, input().split())
ls = list(map(int, input().split()))

left = 0
current_sum = 0
result = N + 1

for right in range(N):
    current_sum += ls[right]
    
    while current_sum >= S:
        result = min(result, right - left + 1)
        current_sum -= ls[left]
        left += 1
        
if result == N+1:
    print(0)

else:
    print(result)