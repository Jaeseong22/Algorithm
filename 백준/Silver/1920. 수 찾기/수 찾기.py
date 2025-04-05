def solution():
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    a = set(map(int, input().strip().split()))
    
    m = int(input())
    b = list(map(int, input().strip().split()))
    
    for num in b:
        print(1) if num in a else print(0)
solution()