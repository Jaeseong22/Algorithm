import sys
input = sys.stdin.readline

x, y = map(int, input().split())

z = (y * 100) // x

if z >= 99:
    print(-1)
    sys.exit()

left, right = 1, 10**9
res = -1

while left <= right:
    mid = (left + right) // 2
    newz = ((y + mid) * 100) // (x + mid)

    if newz > z:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)