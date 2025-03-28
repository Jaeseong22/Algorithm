def solution():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().strip().split())
    card = list(map(int, input().strip().split()))

    result = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if card[i] + card[j] + card[k] > m:
                    continue
                else:
                    result = max(result, card[i] + card[j] + card[k])

    print(result)


solution()