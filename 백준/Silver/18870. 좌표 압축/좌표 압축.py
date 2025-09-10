import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
unique_arr = sorted(set(arr))
index_dict = {unique_arr[i] : i for i in range(len(unique_arr))}
result = [index_dict[x] for x in arr]

print(*result)