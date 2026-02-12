import sys
input = sys.stdin.readline

string = list(input().strip())
bomb = list(input().strip())
length = len(bomb)

res = []

for i in string:
    res.append(i)
    if res[len(res)-length:len(res)] == bomb:
        for _ in range(length):
            res.pop()

if res:
    print(*res, sep='')

else:
    print("FRULA")