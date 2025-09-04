import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)

while low <= high:
    mid = (low + high) // 2
    wood = 0
    for h in trees:
        if h>mid:
            wood += h-mid
    if wood >= m:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)