from collections import deque
import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    result = deque()

    for _ in range(t):
        n, m = map(int, input().split())
        priorities = list(map(int, input().split()))
        dq = deque([(priority, idx) for idx, priority in enumerate(priorities)])
        count = 0

        while dq:
            current = dq.popleft()

            if any(current[0] < other[0] for other in dq):
                dq.append(current)
            else:
                count += 1
                if current[1] == m:
                    result.append(count)
                    break
    for k in result:
        print(k)

solution()