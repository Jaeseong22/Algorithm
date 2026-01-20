from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    visited = [False] * 10000
    how = [''] * 10000
    prev = [-1] * 10000
    
    visited[a] = True
    q = deque()
    q.append(a)
    
    while q:
        cur = q.popleft()
        if cur == b:
            break
        
        d = (cur * 2) % 10000
        if not visited[d]:
            visited[d] = True
            prev[d] = cur
            how[d] = 'D'
            q.append(d)
        
        s = cur - 1 if cur != 0 else 9999
        if not visited[s]:
            visited[s] = True
            prev[s] = cur
            how[s] = 'S'
            q.append(s)
        
        l = (cur%1000) * 10 + (cur // 1000)
        if not visited[l]:
            visited[l] = True
            prev[l] = cur
            how[l] = 'L'
            q.append(l)
        
        r = (cur % 10) * 1000 + (cur // 10)
        if not visited[r]:
            visited[r] = True
            prev[r] = cur
            how[r] = 'R'
            q.append(r)
    
    result = []
    cur = b
    while cur != a:
        result.append(how[cur])
        cur = prev[cur]
    
    print(''.join(reversed(result)))