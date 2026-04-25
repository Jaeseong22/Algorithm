def solution(n, lost, reserve):
    answer = 0
    lost = set(lost)
    reserve = set(reserve)
    
    both = lost & reserve
    lost -= both
    reserve -= both
    
    for r in sorted(reserve):
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    return n - len(lost)