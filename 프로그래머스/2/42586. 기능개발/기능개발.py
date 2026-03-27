def solution(progresses, speeds):
    answer = []
    days = []
    
    for p, s in zip(progresses, speeds):
        days.append((100-p+s-1)//s)
    now = days[0]
    cnt = 1
    for nxt in days[1:]:
        if nxt <= now:
            cnt += 1
        else:
            answer.append(cnt)
            now = nxt
            cnt = 1
    
    answer.append(cnt)
    return answer