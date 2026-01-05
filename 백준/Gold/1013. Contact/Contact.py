import re
import sys
input = sys.stdin.readline

t = int(input())
result = []

for _ in range(t):
    sign = input().strip()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(sign)
    if m:
        result.append("YES")
    else:
        result.append("NO")
        
for i in result:
    print(i)