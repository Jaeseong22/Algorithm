def solution(maps):
    from collections import deque
    INF = int(1e9)
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    distance = [[INF] * (len(maps[0])) for _ in range(len(maps))]
    
    q = deque()
    q.append((0, 0))
    distance[0][0] = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if distance[nx][ny] == INF and maps[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
    
    answer = distance[len(maps)-1][len(maps[0])-1]
    if answer == INF:
        return -1
    else:
        return answer