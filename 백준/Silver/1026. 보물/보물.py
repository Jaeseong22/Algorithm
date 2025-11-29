import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=False)

res = 0
for i in range(n):
    res += a[i]*b[i]
    
print(res)