import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
round = 0
while a != b:
    a = (a + 1) // 2
    b = (b + 1) // 2
    round += 1
    
print(round)