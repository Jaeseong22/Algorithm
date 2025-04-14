from collections import deque
import sys
input = sys.stdin.readline

def solution():
    result = deque()
    vo = ['a', 'e', 'i', 'o', 'u']

    while True:        
        dq = input().strip().lower()
        if dq == '#':
            break

        count = 0
        for i in dq:
            if i in vo:
                count += 1
        result.append(count)
    
    for res in result:
        print(res)

solution()