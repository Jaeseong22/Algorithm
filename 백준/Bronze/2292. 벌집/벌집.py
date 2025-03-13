def solution():
    n = int(input())
    num = 1
    result = 1
    i = 1
    while(n > num):
        num += 6*i
        result += 1
        i+=1
    
    print(result)    

solution()