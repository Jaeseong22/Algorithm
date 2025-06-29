import sys
input = sys.stdin.readline

n = int(input())
r = [0]*1001
r[1] = 1
r[2] = 2
r[3] = 3

for i in range(4, n+1):
    r[i] = r[i-1] + r[i-2]

print(r[n]%10007)