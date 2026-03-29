def solution(clothes):
    ans = {}
    for name, cloth in clothes:
        if cloth not in ans:
            ans[cloth] = 1
        else:
            ans[cloth] += 1
    
    a = 1
    for v in ans.values():
        a *= (v+1)
        
    return a - 1
