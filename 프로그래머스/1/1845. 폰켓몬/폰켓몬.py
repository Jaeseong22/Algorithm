def solution(nums):
    n = len(nums)//2
    num = set(nums)
    s = len(num)
    
    if s > n:
        return n
    
    return s