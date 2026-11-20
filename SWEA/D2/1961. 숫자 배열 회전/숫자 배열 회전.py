T = int(input())

def rotate(g, n):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = g[n-1-j][i]
    return result

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    r90 = rotate(graph, N)
    r180 = rotate(r90, N)
    r270 = rotate(r180, N)
    
    print(f'#{tc}')
    
    for i in range(N):
        a = ''.join(map(str, r90[i]))
        b = ''.join(map(str, r180[i]))
        c = ''.join(map(str, r270[i]))
        print(a, b, c)