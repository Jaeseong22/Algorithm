def solution():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().strip().split())

    chess = [input().strip() for _ in range(n)]
    
    white_first = [
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW'
    ]

    min_paint = 64
    
    for j in range(n-7):
        for i in range(m-7):
            count = 0
            for row in range(8):
                for col in range(8):
                    if chess[j+row][i+col] != white_first[row][col]:
                        count += 1
            min_paint = min(min_paint, count, 64-count)
    print(min_paint)
solution()