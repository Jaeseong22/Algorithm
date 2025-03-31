def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def solution():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().strip().split())

    if k == 0 or k == n:
        print(1)
        return

    n_re = factorial(n)
    k_re = factorial(k)
    nk_re = factorial(n - k)

    result = n_re // (k_re * nk_re)  # 정수 나눗셈 사용
    print(result)

solution()