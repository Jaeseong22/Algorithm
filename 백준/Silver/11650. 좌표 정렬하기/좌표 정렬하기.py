def solution():
    import sys
    input = sys.stdin.readline

    n = int(input())
    re = []

    for i in range(n):
        re.append(tuple(map(int, input().strip().split())))
    
    result = sorted(re, key = lambda x : (x[0], x[1]))
    
    for i in result:
        print(i[0], i[1])
solution()