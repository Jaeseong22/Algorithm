import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

a_s = a_set - b_set
b_s = b_set - a_set
res = a_s | b_s
print(len(res))