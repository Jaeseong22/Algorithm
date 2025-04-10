from collections import deque
import sys
input = sys.stdin.readline

def solution():
    n = int(input())

    result = deque()
    sd = deque()

    for i in range(n):
        appended_cmd = input().strip().split()
        if appended_cmd[0] == 'push':
            sd.append(appended_cmd[1])
        elif appended_cmd[0] == 'pop':
            if not sd:
                result.append(-1)
            else:
                result.append(sd.popleft())
        elif appended_cmd[0] == 'size':
            result.append(len(sd))
        elif appended_cmd[0] == 'empty':
            if not sd:
                result.append(1)
            else:
                result.append(0)
        elif appended_cmd[0] == 'front':
            if not sd:
                result.append(-1)
            else:
                result.append(sd[0])
        elif appended_cmd[0] == 'back':
            if not sd:
                result.append(-1)
            else:
                result.append(sd[-1])
    
    for res in result:
        print(res)

solution()