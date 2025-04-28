from collections import deque
import sys
input = sys.stdin.readline

def solution():
    count = 1
    temp = True
    op = deque()
    n = int(input())
    dq = deque()

    for _ in range(n):
        num = int(input())
        while count <= num:
            dq.append(count)
            op.append('+')
            count += 1

        if dq[-1] == num:
            dq.pop()
            op.append('-')

        else:
            temp = False
            break

    if temp == False:
        print("NO")
    else:
        for i in op:
            print(i)

solution()