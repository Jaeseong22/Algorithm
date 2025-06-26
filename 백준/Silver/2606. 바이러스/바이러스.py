import sys
from collections import defaultdict
input = sys.stdin.readline

computers = int(input())
neighbors = int(input())
visited = [False] * (computers + 1)

dic = defaultdict(list)

for _ in range(neighbors):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [False for _ in range(computers+1)]

def dfs(node):
    visited[node] = True
    for neighbor in dic[node]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(1)
print(sum(visited)-1)
