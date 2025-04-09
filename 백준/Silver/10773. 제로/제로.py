def solution():
    import sys
    input = sys.stdin.readline

    k = int(input())

    sd = []

    for i in range(k):
        n = int(input())
        if n == 0:
            sd.pop()
        else:
            sd.append(n)

    print(sum(sd))

solution()