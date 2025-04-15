from collections import deque
import sys
input = sys.stdin.readline

def solution():
    k, n = map(int, input().split())
    dq = deque()
    for i in range(k):
        a = int(input())
        dq.append(a)
    
    start, end = 1, max(dq)
    
    while start <= end:
        mid = (start + end) // 2
        lines = 0
        for i in dq:
            lines += i // mid

        if lines >= n:
            start = mid + 1
        else:
            end = mid - 1        
    
    print(end)
solution()