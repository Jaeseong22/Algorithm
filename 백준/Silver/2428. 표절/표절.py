import sys
input = sys.stdin.readline

n = int(input())
sol = sorted(map(int, input().split()))
res = 0

for i in range(n-1):
    s, e = i+1, n-1
    t = -1
    while s<=e:
        m = (s+e)//2
        if sol[i] * 10 >= 9*sol[m]:
            t = m
            s = m + 1
        else:
            e = m - 1
    res += t-i if t > -1 else 0
    
print(res)