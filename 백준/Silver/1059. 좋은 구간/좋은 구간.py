import sys
input = sys.stdin.readline

l = int(input())
s = sorted(list(map(int, input().strip().split())))
n = int(input())

if n in s:
    print(0)
else:    
    min = 0
    max = 0
    for i in s:
        if i < n:
            min = i
        elif i > n and max == 0:
            max = i
    print((n-min)*(max-n) - 1)