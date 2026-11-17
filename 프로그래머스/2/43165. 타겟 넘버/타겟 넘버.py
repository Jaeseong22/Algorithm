def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def backtrack(idx, s):
        nonlocal answer
        if idx == n:
            if s == target:
                answer += 1
            return
        
        backtrack(idx + 1, s+numbers[idx])
        backtrack(idx + 1, s-numbers[idx])
    
    backtrack(0, 0)
                    
    return answer