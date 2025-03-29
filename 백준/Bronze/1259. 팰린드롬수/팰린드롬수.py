def solution():
    import sys
    input = sys.stdin.readline
    ls = []
    while True:
        s = input().strip()
        if s == '0':
            break
        ls.append(s)
    
    for i in ls:
        if i == i[::-1]:
            print('yes')
        else:
            print('no')          

solution()