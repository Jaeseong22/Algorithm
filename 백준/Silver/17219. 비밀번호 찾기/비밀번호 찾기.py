import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    site = {}
    result = []

    for _ in range(n):
        name, pw = input().strip().split()
        site[name] = pw
    
    for i in range(m):
        id = input().strip()
        result.append(site[id])
    
    for res in result:
        print(res)

solution()