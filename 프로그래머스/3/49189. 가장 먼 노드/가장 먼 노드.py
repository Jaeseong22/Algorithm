def solution(n, edge):
    from collections import deque
    answer = 0
    graph = {i:[] for i in range(1, n+1)}
    
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    q = deque()
    q.append((0, 1))
    visited = [-1] * (n+1)
    visited[1] = 0
    
    while q:
        w, now = q.popleft()
        
        for nxt in graph[now]:
            if visited[nxt] == -1:
                q.append((w+1, nxt))
                visited[nxt] = w+1
    
    max_answer = max(visited)
    
    for i in visited:
        if i == max_answer:
            answer += 1
    
    return answer