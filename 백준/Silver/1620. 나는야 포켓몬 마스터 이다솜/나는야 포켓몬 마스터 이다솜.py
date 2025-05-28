import sys
from collections import deque
input = sys.stdin.readline

def solution():
    dic = {}
    rev_dic = {}
    result = deque()
    
    n, m = map(int, input().split())

    for i in range(1, n+1):
        poke = input().strip()
        dic[str(i)] = poke
        rev_dic[poke] = str(i)

    for j in range(m):
        inp = input().strip()
        if inp.isdigit():
            result.append(dic[inp])
        else:
            result.append(rev_dic[inp])

    for res in result:
        print(res)
 
solution()