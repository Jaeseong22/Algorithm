import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
res = []

for i in range(m, n+1):
    if i == 1:
        continue
    is_s = True
    for j in range(2, i):
        if i % j == 0:
            is_s = False
            break
    if is_s:
       res.append(i)

if (len(res)>0):
    print(sum(res))
    print(min(res)) 
else:
    print(-1)