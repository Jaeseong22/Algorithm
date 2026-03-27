def solution(citations):
    answer = 0
    
    for h in range(len(citations) + 1):
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
        if cnt >= h:
            answer = h
    
    return answer