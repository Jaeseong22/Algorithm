def solution():
    import sys
    input = sys.stdin.readline

    result = []
    while True:
        line = input().rstrip()
        if line == '.':
            break

        stack = []
        balanced = True

        for char in line:
            if char == '(' or char == '[':
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                    balanced = False
                    break
                stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    balanced = False
                    break
                stack.pop()

        if balanced and not stack:
            result.append('yes')
        else:
            result.append('no')
    for i in result:
        print(i)

solution()