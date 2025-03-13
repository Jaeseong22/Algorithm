def solution():
    m = int(input())
    for i in range(1, m+1):
        num = sum(map(int, str(i)))
        num_sum = i + num

        if num_sum == m:
            print(i)
            break
        if i == m:
            print(0)
solution()