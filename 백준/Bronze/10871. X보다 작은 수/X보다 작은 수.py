def solution():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    result = []
    for i in a:
        if(x > i):
            result.append(i)
    print(*result)
solution()