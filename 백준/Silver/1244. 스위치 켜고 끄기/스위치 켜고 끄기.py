import sys
input = sys.stdin.readline

switch_n = int(input())
switchs = list(map(int, input().split()))
student_n = int(input())

for _ in range(student_n):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(num - 1, switch_n, num):
            switchs[i] = 1 - switchs[i]

    else:
        left = right = num - 1

        while left - 1 >= 0 and right + 1 < switch_n and switchs[left - 1] == switchs[right + 1]:
            left -= 1
            right += 1

        for i in range(left, right + 1):
            switchs[i] = 1 - switchs[i]

for i in range(switch_n):
    print(switchs[i], end=' ')
    if (i + 1) % 20 == 0:
        print()