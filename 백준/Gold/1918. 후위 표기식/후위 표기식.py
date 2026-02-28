import sys
input = sys.stdin.readline

mid = list(input().strip())
stack = []
result = []
priority = {
    '(' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}

for cmd in mid:
    if cmd.isalpha():
        result.append(cmd)
    elif cmd == '(':
        stack.append(cmd)
    elif cmd == ')':
        while stack[-1] != '(' and stack:
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and priority[cmd] <= priority[stack[-1]]:
            result.append(stack.pop())
        stack.append(cmd)
    
while stack:
    result.append(stack.pop())

print(''.join(result))