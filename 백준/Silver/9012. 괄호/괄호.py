def solution():
    import sys
    input = sys.stdin.readline

    t = int(input())

    sd = []
    for _ in range(t):
        n = input().strip()
        sd.append(n)

    result = []
    for i in sd:
        ind = True
        index1 = []

        for char in i:
            if char == '(':
                index1.append(char)
            elif char == ')':
                if not index1 or index1[-1] != '(':
                    ind = False
                    break
                index1.pop()
        
        if index1:
            ind = False
        
        if ind:
            result.append('YES')
        
        else:
            result.append('NO')

    for re in result:
        print(re)
            
solution()