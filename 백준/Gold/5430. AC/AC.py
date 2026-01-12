from collections import deque
import sys
input = sys.stdin.readline
res = []
t = int(input())
for _ in range(t):
    funcs = input().strip()
    n = int(input())
    arr = input().strip()
    
    if arr == "[]":
        lis = deque()
    else:
        lis = deque(arr[1:-1].split(','))
    
    rev = False
    error = False
    
    for func in funcs:
        if func == 'R':
            rev = not rev
        else:
            if not lis:
                print("error")
                error = True
                break
            if not rev:
                lis.popleft()
            else:
                lis.pop()
    if error:
        continue
    if rev:
        lis.reverse()
    print("[" + ",".join(lis)+"]")