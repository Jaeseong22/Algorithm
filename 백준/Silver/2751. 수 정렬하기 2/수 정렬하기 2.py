def solution():
    import sys
    input = sys.stdin.readline

    n = int(input())
    result = []
    for i in range(n):
        result.append(int(input()))

    result2 = sorted(result, reverse=False)
    for i in result2:
        print(i)
solution()