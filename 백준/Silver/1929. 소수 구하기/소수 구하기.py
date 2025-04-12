import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    for i in range(n, m+1):
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)

solution()