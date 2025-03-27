def solution():
    n = int(input())
    ls = []
    for i in range(n):
        weight, height = map(int, input().split())
        ls.append([weight, height])
    ls1 = []
    for j in range(n):
        cur = 1 
        for k in range(n):
            if(ls[j][0] < ls[k][0]):
                if(ls[j][1] < ls[k][1]):
                    cur += 1
        ls1.append(cur)        

    print(*ls1)
solution()