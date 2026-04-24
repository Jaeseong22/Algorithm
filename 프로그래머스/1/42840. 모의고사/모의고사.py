def solution(answers):
    f = [1, 2, 3, 4, 5]
    s = [2, 1, 2, 3, 2, 4, 2, 5]
    t = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    dic = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if f[i % len(f)] == answers[i]:
            dic[1] += 1
        if s[i % len(s)] == answers[i]:
            dic[2] += 1
        if t[i % len(t)] == answers[i]:
            dic[3] += 1
            
    max_score = max(dic.values())
    
    result = []
    for person, cnt in dic.items():
        if cnt == max_score:
            result.append(person)
        
    return result