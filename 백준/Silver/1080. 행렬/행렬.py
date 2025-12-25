import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
b = [list(input().strip()) for _ in range(n)]

def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = '1' if a[i][j] == '0' else '0'

cnt = 0

if (n<3 or m<3) and a != b:
    cnt = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                flip(i, j)
                cnt += 1

if cnt != -1:
    if a != b:
        cnt = -1

print(cnt)