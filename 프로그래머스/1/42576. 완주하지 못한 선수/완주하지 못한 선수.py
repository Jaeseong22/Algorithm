def solution(participant, completion):
    answer = ''
    win = {}
    lose = {}
    
    for p in participant:
        if p not in win:
            win[p] = 1
        else:
            win[p] += 1
    
    for p in completion:
        if p not in lose:
            lose[p] = 1
        else:
            lose[p] += 1
    
    for n, w in win.items():
        if n not in lose:
            answer = n
        else:
            if lose[n] != w:
                answer = n
                
    return answer