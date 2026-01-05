import sys
import re
input = sys.stdin.readline
p = re.compile('(100+1+|01)+')

sign = input().strip()
m = p.fullmatch(sign)
if m:
    print("SUBMARINE")
else:
    print("NOISE")