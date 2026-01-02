import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input().strip()))
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0

def dfs(x, y, distance):
    global answer
    
    if x == 0 and y == c-1:
        if distance == k:
            answer += 1
        return
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
            graph[nx][ny] = 'T'
            dfs(nx, ny, distance + 1)
            graph[nx][ny] = '.'

graph[r-1][0] = 'T'
dfs((r-1), 0, 1)

print(answer)