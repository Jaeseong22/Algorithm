from collections import deque

def solution():
    import sys
    input = sys.stdin.readline

    n = int(input())
    sd = deque([i for i in range(1, n+1)])

    
    while len(sd) > 1:
        sd.popleft()
        move_num = sd.popleft()
        sd.append(move_num)

    print(*sd)    


solution()