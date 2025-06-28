import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = [0]*101
    p[1] = 1
    p[2] = 1
    p[3] = 1
    n = int(input())

    if n>3:
        for i in range(4, n+1):
            p[i] = p[i-3] + p[i-2]
    
    print(p[n])