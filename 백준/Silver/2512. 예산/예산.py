import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

sum_b = sum(budget)

if sum_b <= m:
    print(max(budget))
else:
    left, right = 0, max(budget)
    res = 0
    
    while left <= right:
        mid = (left+right)//2
        total = 0
        for x in budget:
            total += x if x <= mid else mid
        
        if total <= m:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    print(res)