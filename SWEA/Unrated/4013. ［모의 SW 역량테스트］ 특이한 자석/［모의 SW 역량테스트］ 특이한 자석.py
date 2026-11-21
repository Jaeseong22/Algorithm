T = int(input())

def rt(g, d):
    if d == 1:
        return [g[-1]] + g[:-1]
    else:
        return g[1:] + [g[0]]

for tc in range(1, T+1):
    k = int(input())
    graph = [list(map(int, input().split())) for _ in range(4)]
    
    for _ in range(k):
        n, d = map(int, input().split())
        n -= 1
        
        dirs = [0] * 4
        dirs[n] = d
        
        for i in range(n+1, 4):
            if graph[i-1][2] != graph[i][6]:
                dirs[i] = -dirs[i-1]
            else:
                break
        
        for i in range(n-1, -1, -1):
            if graph[i][2] != graph[i+1][6]:
                dirs[i] = -dirs[i+1]
            else:
                break
        
        for i in range(4):
            if dirs[i] != 0:
                graph[i] = rt(graph[i], dirs[i])
        
    score = 0
    for i in range(4):
        if graph[i][0] == 1:
            score += 2**i
    print(f'#{tc} {score}')