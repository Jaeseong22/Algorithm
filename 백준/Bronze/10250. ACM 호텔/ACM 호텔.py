def solution():
    t = int(input())
    ls = []

    for i in range(t):
        h, w, n = map(int, input().split())
        dec = 1
        while n > h:
            dec += 1
            n = n - h

        result = dec + (n)*100
        ls.append(result)

    for i in ls:
        print(i)
        

solution()