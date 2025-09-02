import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0]  # [하얀색(0) 개수, 파란색(1) 개수]

def div(x, y, size):
    color = paper[y][x]
    # 영역이 단색인지 확인
    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != color:
                m = size // 2
                # 좌상, 우상, 좌하, 우하
                div(x, y, m)
                div(x + m, y, m)
                div(x, y + m, m)
                div(x + m, y + m, m)
                return
    # 단색이면 카운트
    result[color] += 1

div(0, 0, n)
print(result[0])  # 하얀색
print(result[1])  # 파란색