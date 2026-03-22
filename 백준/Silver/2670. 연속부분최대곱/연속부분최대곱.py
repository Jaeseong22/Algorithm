import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    a = float(input())
    nums.append(a)

for i in range(1, N):
    nums[i] = max(nums[i], (nums[i-1]*nums[i]))

print('%0.3f' %max(nums))