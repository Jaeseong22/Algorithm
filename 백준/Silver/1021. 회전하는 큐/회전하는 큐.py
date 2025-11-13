from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lis = list(map(int, input().split()))
dq = deque([x for x in range(1, n+1)])
result = 0

for nu in lis:
    while True:
        if dq[0] == nu:
            dq.popleft()
            break
        else:
            if dq.index(nu) < len(dq)/2:
                while dq[0] != nu:
                    dq.append(dq.popleft())
                    result += 1
            else:
                while dq[0] != nu:
                    dq.appendleft(dq.pop())
                    result += 1

print(result)