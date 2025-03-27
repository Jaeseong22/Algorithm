import sys
input = sys.stdin.readline
# data = input().splitlines()

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().strip().split())
    points.append((x, y))

result = sorted(points, key=lambda p: (p[1], p[0]))


for i in result:
    print(i[0], i[1])