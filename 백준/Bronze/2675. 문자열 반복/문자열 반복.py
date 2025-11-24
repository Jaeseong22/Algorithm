import sys
input = sys.stdin.readline

t = int(input())

a = []
for i in range(t):
    r, s = input().split()
    res = ''
    for j in s:
        res += j*int(r)
    a.append(res)
    
for i in a:
    print(i)