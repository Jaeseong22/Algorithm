import sys
input = sys.stdin.readline

n = int(input())
res = []

for _ in range(n):
    res.append(input().strip())
    
cnt = 1
while(1):
    if len(set(i[-cnt:] for i in res)) == n:
        print(cnt)
        break
    else:
        cnt += 1