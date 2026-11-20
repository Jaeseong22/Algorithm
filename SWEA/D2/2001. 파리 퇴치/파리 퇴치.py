T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    tmp += graph[k][l]
            ans = max(ans, tmp)
    
    print(f"#{tc} {ans}")