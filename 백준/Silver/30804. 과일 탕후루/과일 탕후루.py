import sys
input = sys.stdin.readline

n = int(input())
frts = list(map(int, input().split()))
count = {}
dist = 0
ans = 0
left = 0

for right in range(n):
    if frts[right] in count:
        count[frts[right]] += 1
    else:
        count[frts[right]] = 1
        dist += 1
    while dist > 2:
        count[frts[left]] -= 1
        if count[frts[left]] == 0:
            del count[frts[left]]
            dist -= 1
        left += 1
    ans = max(ans, right - left + 1)

print(ans)