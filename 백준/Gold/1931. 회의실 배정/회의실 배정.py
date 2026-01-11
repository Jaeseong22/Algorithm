import sys
input = sys.stdin.readline

n = int(input())
lis = []
for _ in range(n):
    start, end = map(int, input().split())
    lis.append((start, end))

lis = sorted(lis, key = lambda x: (x[1], x[0]))
cnt = 1

n_en = lis[0][1]
for i in range(1, n):
    if lis[i][0] >= n_en:
        n_en = lis[i][1]
        cnt +=1

print(cnt)