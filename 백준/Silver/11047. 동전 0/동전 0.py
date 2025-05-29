import sys
from collections import deque
input = sys.stdin.readline


def solution():
    n, k = map(int, input().strip().split())
    dq = deque()
    
    for _ in range(n):
        dq.append(int(input()))
    dq = sorted(dq, reverse=True)
    cnt = 0
    for i in dq:
        if k >= i:
            cnt += k // i
            k %= i
            if k <= 0:
                break
    print(cnt)

solution()