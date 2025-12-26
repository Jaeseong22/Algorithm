import sys
input = sys.stdin.readline

b = [int(input()) for _ in range(9)]
db = sum(b) - 100

found = False
for i in range(9):
    for j in range(i+1, 9):
        if b[i] + b[j] == db:
            b.pop(j)
            b.pop(i)
            found = True
            break
    if found:
        break

b.sort()
for x in b:
    print(x)