import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

num = [0] * 10

abc = a*b*c

str_abc = list(str(abc))

for i in str_abc:
    num[int(i)] += 1
    
for i in num:
    print(i)