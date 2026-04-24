def solution(k, dungeons):
    answer = 0
    visited = [False] * (len(dungeons))
    
    def dfs(cur_fatigue, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            need, cost = dungeons[i]
            if not visited[i] and cur_fatigue >= need:
                visited[i] = True
                dfs(cur_fatigue - cost, count+1)
                visited[i] = False
    dfs(k, 0)
    
    return answer