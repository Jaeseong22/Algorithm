import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
res = 0

for i in range(n):
    if nums[i] == 1:
        continue
    else:
        is_so = True
        for j in range(2, nums[i]):
            if nums[i] % j == 0:
                is_so = False
                break
        if is_so:
            res += 1

print(res)