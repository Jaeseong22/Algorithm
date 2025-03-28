def solution():
    import sys
    input = sys.stdin.readline

    n = int(input())
    result_ls = []
    od_ls = list(map(int, input().strip().split()))
    
    for i in od_ls:
        if i<2:
            continue
        is_prime = True
        for j in range(2, int(i)):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            result_ls.append(i)

    print(len(result_ls))
solution()