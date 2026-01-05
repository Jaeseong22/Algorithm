import sys
input = sys.stdin.readline

t = int(input())
result = []
for _ in range(t):
    x, y = map(int, input().split())
    
    distance = y-x
    step = 1
    cnt = 0
    mydist = 0
    
    while mydist < distance:
        cnt += 1
        mydist += step
        
        if cnt % 2 == 0:
            step += 1
    result.append(cnt)
    
for i in result:
    print(i)