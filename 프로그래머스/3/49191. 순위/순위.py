def solution(n, results):
    answer = 0
    win_graph = {i:[] for i in range(1, n+1)}
    lose_graph = {i:[] for i in range(1, n+1)}
    for a, b in results:
        win_graph[a].append(b)
        lose_graph[b].append(a)
        
    def dfs(graph, start):
        visited = [False] * (n+1)
        visited[start] = True
        
        stack = [start]
        cnt = 0
        
        while stack:
            now = stack.pop()
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
                    cnt += 1
        return cnt
    
    for i in range(1, n+1):
        win_cnt = dfs(win_graph, i)
        lose_cnt = dfs(lose_graph, i)
        if win_cnt + lose_cnt == n-1:
            answer += 1
        
    return answer