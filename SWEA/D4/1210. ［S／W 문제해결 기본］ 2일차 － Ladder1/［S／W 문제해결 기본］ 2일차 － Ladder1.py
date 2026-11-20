for _ in range(10):
    t = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    x = graph[99].index(2)
    y = 99
    
    while y > 0:
        if x > 0 and graph[y][x-1] == 1:
            while x > 0 and graph[y][x-1] == 1:
                x -= 1
        elif x < 99 and graph[y][x+1] == 1:
            while x < 99 and graph[y][x+1] == 1:
                x += 1
        y -= 1
    
    print(f"#{t} {x}")