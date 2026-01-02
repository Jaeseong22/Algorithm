import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
operator = list(map(int, input().split()))

def dfs(level, result, add, sub, mul, div):
    global maximum, minimum
    
    if level == n:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        
    if add != 0:
        dfs(level+1, result+a[level], add-1, sub, mul, div)
    if sub != 0:
        dfs(level+1, result-a[level], add, sub-1, mul, div)
    if mul != 0:
        dfs(level+1, result*a[level], add, sub, mul-1, div)
    if div != 0:
        dfs(level+1, int(result/a[level]), add, sub, mul, div-1)
        
maximum = -1e9
minimum = 1e9
    
dfs(1, a[0], operator[0], operator[1], operator[2], operator[3])

print(maximum)
print(minimum)