def solution(n, computers):
    answer = 0
    visited = [False] * n
    def dfs(i):
        stack = [i]
        
        while stack:
            now = stack.pop()
            visited[now] = True
            for j in range(n):
                if computers[now][j] and not visited[j]:
                    stack.append(j)
    
    cnt = 0
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)
    
    answer = cnt
            
    return answer