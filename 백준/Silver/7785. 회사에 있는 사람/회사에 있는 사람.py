import sys
input = sys.stdin.readline

n = int(input())
worker = {}

for _ in range(n):
    name, working = input().split()
    worker[name] = working

answer = []

answer = sorted([name for name in worker if worker[name] == 'enter'], reverse=True)

for a in answer:
    print(a)