from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dq = deque([i for i in range(1, n+1)])
result = []

while True:
    if len(dq) == 1:
        result.append(dq.popleft())
        break
    else:
        dq.rotate(-(k-1))
        result.append(dq.popleft())

print(f"<{', '.join(map(str, result))}>")
