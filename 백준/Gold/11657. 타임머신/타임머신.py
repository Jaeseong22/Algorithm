import sys
INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

distance = [INF] * (N+1)

def bf(start):
    distance[start] = 0
    for i in range(1, N+1):
        for S, E, W in edges:
            if distance[S] != INF and distance[E] > distance[S] + W:
                distance[E] = distance[S] + W
                if i == N:
                    return True
    return False

if bf(1):
    print(-1)
else:
    for i in distance[2:]:
        if i != INF:
            print(i)
        else:
            print(-1)