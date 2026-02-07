import sys
input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input().strip()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

stack = [(0, 0, set(graph[0][0]), 1)]
answer = 1

while stack:
    x, y, used, length = stack.pop()
    answer = max(answer, length)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] not in used:
                stack.append((nx, ny, used | {graph[nx][ny]}, length+1))
                
print(answer)