import heapq
import math
import sys
input = sys.stdin.readline

n = int(input())
max_heap = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(max_heap, (math.fabs(x), x))
    else:
        if max_heap:
            a = heapq.heappop(max_heap)[1]
            print(a)
        else:
            print(0)