def solution():
    n = int(input())
    for i in range(n, 0, -1):
        print(' '*(i-1)+"*"*(n-i+1))

solution()