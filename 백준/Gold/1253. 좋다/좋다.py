import sys
input = sys.stdin.readline

n = int(input())
res = list(map(int, input().strip().split()))
res.sort()

cnt = 0
for i in range(n):
    target = res[i]
    left, right = 0, n-1
    
    
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        s = res[left] + res[right]
        if s == target:
            cnt += 1
            break
        elif s < target:
            left += 1
        else:
            right -= 1

print(cnt)