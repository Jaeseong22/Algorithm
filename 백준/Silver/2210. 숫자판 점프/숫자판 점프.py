import sys
input = sys.stdin.readline

result = set()
graph = [list(input().split()) for _ in range(5)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, level, nums):
    if level == 6:
        result.add(nums)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, level+1, nums + graph[nx][ny])
            
for i in range(5):
    for j in range(5):
        dfs(i, j, 1, graph[i][j])
        
print(len(result))