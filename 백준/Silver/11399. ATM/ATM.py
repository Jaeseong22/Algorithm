import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n = int(input().strip())
    p = deque(map(int, input().split()))
    p = sorted(p)
    
    sum = 0
    for i in range(1, n+1):
        for j in range(i):
            sum += p[j]
    print(sum)

solution()
    