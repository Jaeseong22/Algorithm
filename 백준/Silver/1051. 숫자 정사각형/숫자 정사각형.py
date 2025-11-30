import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

max_size = 0  # (한 변 - 1) 값, 최소는 0 -> 1x1

# size: 한 변에서 줄어드는 값이 아니라, (끝 인덱스 - 시작 인덱스)
for size in range(0, min(N, M)):
    for i in range(N - size):
        for j in range(M - size):
            # 네 꼭짓점 비교
            if (board[i][j] == board[i + size][j] and
                board[i][j] == board[i][j + size] and
                board[i][j] == board[i + size][j + size]):
                if size > max_size:
                    max_size = size

# 실제 한 변 길이는 max_size + 1
answer = (max_size + 1) ** 2
print(answer)