from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 진실 아는 사람들
data = list(map(int, input().split()))
t = data[0]
truth = set(data[1:]) if t > 0 else set()

parties = []

for _ in range(m):
    line = list(map(int, input().split()))
    k = line[0]
    members = line[1:]
    parties.append(members)

# 진실 전파
changed = True
while changed:
    changed = False
    for members in parties:
        if truth & set(members):
            before = len(truth)
            truth |= set(members)
            if len(truth) > before:
                changed = True

# 거짓말 가능한 파티 수
count = 0
for members in parties:
    if not (truth & set(members)):
        count += 1

print(count)