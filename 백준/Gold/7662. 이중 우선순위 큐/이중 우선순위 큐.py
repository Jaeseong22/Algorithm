import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    count = defaultdict(int)
    
    size = 0
    
    for _ in range(k):
        cmd, num = input().split()
        num = int(num)
        
        if cmd == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            count[num] += 1
            size += 1
        else:
            if size == 0:
                continue
            if num == 1:
                while max_heap:
                    x = -heapq.heappop(max_heap)
                    if count[x] > 0:
                        count[x] -= 1
                        size -= 1
                        break
            else:
                while min_heap:
                    x = heapq.heappop(min_heap)
                    if count[x] > 0:
                        count[x] -= 1
                        size -= 1
                        break

    if size == 0:
        print('EMPTY')
    else:
        while max_heap and count[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        while min_heap and count[min_heap[0]] == 0:
            heapq.heappop(min_heap)
        
        print(-max_heap[0], min_heap[0])