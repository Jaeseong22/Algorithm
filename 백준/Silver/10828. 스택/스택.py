from collections import deque

def solution():
    import sys
    input = sys.stdin.readline

    n = int(input())
    dq = deque()

    result = deque()
    for _ in range(n):
        command = input().strip().split()

        if command[0] == 'push':
            dq.append(command[1])
        elif command[0] == 'top':
            result.append((dq[-1] if dq else -1))
        elif command[0] == 'pop':
            if dq:
                result.append((dq.pop()))
            else:
                result.append((-1))
        elif command[0] == 'size':
            result.append((len(dq)))
        elif command[0] == 'empty':
            result.append((0 if dq else 1))

    for res in result:
        print(res)
solution()