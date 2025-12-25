import sys
input = sys.stdin.readline

n = int(input())

if n<100:
    print(n)
elif n == 1000:
    print(144)
else:
    result = 99
    for i in range(100, n+1):
        a = i//100
        b = (i%100)//10
        c = i%10
        if a-b == b-c:
            result += 1
    print(result)