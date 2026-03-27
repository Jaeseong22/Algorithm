def solution(s):
    answer = True
    stack = []
    for st in s:
        if st == '(':
            stack.append(st)
        else:
            if not stack or stack[-1] != '(':
                answer = False
                break
            else:
                stack.pop()
    if stack:
        answer = False
    return answer