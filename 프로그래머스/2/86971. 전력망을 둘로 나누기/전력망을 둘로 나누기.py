def solution(n, wires):
    answer = float('inf')
    
    for cut_a, cut_b in wires:
        w = {i:[] for i in range(1, n+1)}
        
        for x, y in wires:
            if (x == cut_a and y == cut_b) or (x == cut_b and y == cut_a):
                continue
            w[x].append(y)
            w[y].append(x)
        visited = [False] * (n+1)
        
        def dfs(start):
            stack = [(start)]
            visited[start] = True
            cnt = 1
            
            while stack:
                now = stack.pop()
                for nxt in w[now]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        stack.append((nxt))
                        cnt += 1
            return cnt
        
        graph1 = dfs(1)
        graph2 = n - graph1
        
        answer = min(answer, abs(graph1 - graph2))
    
    return answer