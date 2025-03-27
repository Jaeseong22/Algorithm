def solution():
    n = int(input())
    res = 1
    for i in range(1, n+1):
        res *= i
    
    l = 0
    for i in reversed(str(res)):
        if(i != '0'):
            print(l)
            break
        l += 1
        
solution()