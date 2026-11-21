T = int(input())

cmds = ['+', '-', '*', '/']

def cal(a, b, cmd):
    if cmd == 0:
        return a + b
    elif cmd == 1:
        return a - b
    elif cmd == 2:
        return a * b
    else:
        return int(a/b)
    
def backtrack(cnt, ans):
    if cnt >= N-1:
        global max_n, min_n
        if ans > max_n:
            max_n = ans
        if ans < min_n:
            min_n = ans
        return

    for i in range(4):
        if _cmds[i]:
            _cmds[i] -= 1
            backtrack(cnt+1, cal(ans, nums[cnt+1], i))
            _cmds[i] += 1
            
        

for tc in range(1, T+1):
    N = int(input())
    #2 1 0 1
    _cmds = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    max_n = -float('inf')
    min_n = float('inf')
    
    backtrack(0, nums[0])
    print(f'#{tc} {max_n - min_n}')