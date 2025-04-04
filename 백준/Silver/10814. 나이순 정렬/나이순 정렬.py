def solution():
    import sys
    input = sys.stdin.readline

    n = int(input())
    re = []

    for i in range(n):
        age, name = input().split()
        re.append([int(age), name])
    
    result = sorted(re, key = lambda x: x[0])
    for i in result:
        print(i[0], i[1])
solution()