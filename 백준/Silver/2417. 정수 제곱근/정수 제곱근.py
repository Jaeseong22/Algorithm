import sys
input = sys.stdin.readline

n = int(input())

left, right = 0, n
res = 0

while left <= right:
    mid = (left+right) // 2
    if mid * mid >= n:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)