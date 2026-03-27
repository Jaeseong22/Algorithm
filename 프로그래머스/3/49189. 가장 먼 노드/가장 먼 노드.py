def solution(n, edge):
    from collections import deque
    answer = 0
    stack = [[] for _ in range(n+1)]
    for start, nxt in edge:
        stack[start].append(nxt)
        stack[nxt].append(start)
    
    q = deque()
    q.append((0, 1))
    visited = [-1] * (n+1)
    visited[1] = 0
    
    while q:
        w, now = q.popleft()
        
        for nxt in stack[now]:
            if visited[nxt] == -1:
                q.append((w+1, nxt))
                visited[nxt] = w+1
    
    ax = max(visited)
    for i in visited:
        if i == ax:
            answer += 1
    return answer