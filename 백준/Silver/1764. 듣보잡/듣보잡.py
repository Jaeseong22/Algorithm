import sys

input = sys.stdin.readline

def solution():
    n, m = map(int, input().strip().split())
    dq = set()
    result = []

    for _ in range(n):
        word = input().strip()
        dq.add(word)

    for i in range(m):
        n_wor = input().strip()
        if n_wor in dq:
            result.append(n_wor)
        
    result.sort()
    print(len(result))

    for res in result:
        print(res)

solution()