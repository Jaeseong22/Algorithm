def solution():
    import sys
    input = sys.stdin.readline
    ls1 = []
    ls2 = []
    
    while True:
        x, y, z = map(int, input().strip().split())
        if (x, y, z) == (0, 0, 0):
            break
        
        if x > y and x > z:
            if x*x == y*y + z*z:
                ls2.append('right')
            else:
                ls2.append('wrong')
        elif y > x and y > z:
            if y*y == x*x + z*z:
                ls2.append('right')
            else:
                ls2.append('wrong')
        elif z > x and z > y:
            if z*z == x*x + y*y:
                ls2.append('right')
            else:
                ls2.append('wrong')

    for result in ls2:
        print(result)

solution()