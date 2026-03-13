import sys
input = sys.stdin.readline

C, N = map(int, input().split()) # C = 원하는 인원, N = 홍보할 수 잇는 도시의 수

city = [list(map(int, input().split())) for _ in range(N)] # 비용, 얻을 수 있는 고객의 수를 리스트로 저장
INF = int(1e9)
dp = [INF] * (C + 1000)
dp[0] = 0

for cost, plus in city:
    for i in range(plus, C+1000):
        dp[i] = min(dp[i], dp[i - plus] + cost)

print(min(dp[C:]))