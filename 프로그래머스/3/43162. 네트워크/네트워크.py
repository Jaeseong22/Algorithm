def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(a):
        q = [a]
        
        while q:
            now = q.pop()
            visited[now] = True
            
            for i in range(n):
                if computers[now][i] == 1 and not visited[i]:
                    q.append(i)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer