from collections import deque, Counter

def solution():
    import sys
    input = sys.stdin.readline

    n = int(input())
    dq = deque(map(int, input().split()))

    m = int(input())
    dq2 = deque(map(int, input().split()))

    counter = Counter(dq)

    result = deque(counter[num] for num in dq2)
    print(*result)

solution()