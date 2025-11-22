import sys
input = sys.stdin.readline

n = int(input())

res = [0]*n

for i in range(n):
    res[i] = (list(map(int, input().split())))
    
for i in range(1, n):
    res[i][0] = min(res[i-1][1], res[i-1][2]) + res[i][0]
    res[i][1] = min(res[i-1][0], res[i-1][2]) + res[i][1]
    res[i][2] = min(res[i-1][0], res[i-1][1]) + res[i][2]
    
print(min(res[n-1][0], res[n-1][1], res[n-1][2]))