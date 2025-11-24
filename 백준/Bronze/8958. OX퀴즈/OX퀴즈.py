import sys
input = sys.stdin.readline

def sol(n):
    if n==0:
        return 0
    a = 0
    for i in range(1, n+1):
        a += i
    return a

t = int(input())
res = [0] * t

for j in range(t):
    a = list(input().strip())
    a_len = len(a)
    count = 0
    for i in range(len(a)):
        if a[i] == 'O':
            if i == (len(a)-1):
                count += 1
                res[j] += sol(count)
            else:
                count += 1
        else:
            res[j] += sol(count)
            count = 0
        
for i in res:
    print(i)