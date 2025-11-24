import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
num_as = [x for x in range(1, 9)]
num_ds = [x for x in range(8, 0, -1)]

if a == num_as:
    print("ascending")
elif a == num_ds:
    print("descending")
else:
    print("mixed")