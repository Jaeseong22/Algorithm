import sys
input = sys.stdin.readline
INF = int(1e9)

TC = int(input())        
    
for _ in range(TC):
    N, M, W = map(int, input().split())
    roads = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        roads.append((S, E, T))
        roads.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        roads.append((S, E, -T))
    
    distance = [0] * (N+1)
    
    has_circle = False
    for i in range(1, N+1):
        for S, E, T in roads:
            if distance[E] > distance[S] + T:
                distance[E] = distance[S] + T
                if i == N:
                    has_circle = True
    if has_circle:
        print("YES")
    else:
        print("NO")